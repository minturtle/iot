import React, { useEffect, useState } from 'react';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import api from '../api';

function Attendance(){
    const [isLoading, setLoading] = useState(false);
    const [classroom, setClassroom] = useState("");


    const handleClick = () => setLoading(true);

    useEffect(() => {
        if (isLoading) {
            api.attendanceApi(classroom).then(res=>{
                setLoading(false);
                const resultdiv = document.getElementById("attendance_result")
                
                if(res.data.CODE == 33) resultdiv.innerHTML = `<br/><p>해당 강의실과 연결된 라즈베리파이가 없습니다.</p>`
                else resultdiv.innerHTML = `<br/><h5>출석체크 결과</h5>
                <p>${res.data.COUNT}명이 출석했습니다.</p>`
            }).catch(()=>setLoading(false));

        }
      }, [isLoading]);


    return (
        <>
            <h4>실시간 출석체크</h4>
            <Form.Group className="mb-3">
                <Form.Label>강의실</Form.Label>
                <Form.Control type="text" placeholder="D127, DB132..." 
                onChange={e=>setClassroom(e.target.value)} style={{"width" : "50%"}}/>
            </Form.Group>

            <Button
            variant="outline-primary"
            disabled={isLoading}
            onClick={!isLoading ? handleClick : null}>
            {isLoading ? 'Loading…' : '출석체크 요청하기'}
            </Button>
            <div id="attendance_result"></div>
        </>

    )
}

export default Attendance