import React, { useEffect, useState } from 'react';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import api from '../api';


function ClassTime(){

    const [isLoading, setLoading] = useState(false);
    const [classroom, setClassroom] = useState("");
    const [dayweek, setDayweek] = useState("월");
    const [period , setPeriod] = useState("1");

    const handleClick = () => setLoading(true);

    const dayweeks = ["월", "화", "수", "목", "금", "토", "일"]
    const periods = ["1", "2", "3", "4", "5", "6", "7", "8", '9', "A", "B", "C"]
    useEffect(() => {
        if (isLoading) {
          getClassTime().then((result) => {
            setLoading(false);
            if(result.CODE == "21"){
              let body = result.BODY;
              document.getElementById("search_result").innerHTML = `
              <br />
              <h5>조회 결과</h5>
              <p> 과목 코드 : ${body.code}</p>
              <p> 과목 이름 : ${body.class_name}</p>
              <p> 수강 학년 : ${body.grade}</p>
              <p> 교수명 : ${body.professor_name}</p>
              <p> 학점 : ${body.score}</p>`
            }
            else{
              document.getElementById("search_result").innerHTML = "<br /><h5>수업을 조회할 수 없습니다.</h5>";
            }
        
        }
          
          );
        }
      }, [isLoading]);

      const getClassTime = async ()=>{
        return api.classTimeApi(classroom, dayweek, period);
      }


      return(
      <>
        <Form>
          <Form.Group className="mb-3">
            <Form.Label>강의실</Form.Label>
            <Form.Control type="text" placeholder="D127, DB132..." 
            onChange={e=>setClassroom(e.target.value)} style={{"width" : "50%"}}/>
          </Form.Group>
        
        
        <Form.Label>요일</Form.Label>
        <Form.Select onChange={e=>setDayweek(e.target.value)} style={{"width" : "50%"}}>
          {dayweeks.map(dayweek=><option >{dayweek}</option>)}
        </Form.Select><br />

        <Form.Label>시간표</Form.Label>
        <Form.Select onChange={e=>setPeriod(e.target.value)} style={{"width" : "50%"}}>
          {periods.map(p=><option>{p}</option>)}
        </Form.Select><br />
        </Form>
      <Button
            variant="outline-primary"
            disabled={isLoading}
            onClick={!isLoading ? handleClick : null}>
            {isLoading ? 'Loading…' : '시간표 조회하기'}
      </Button>
      <div id="search_result"></div>
      </>
      )
}

export default ClassTime