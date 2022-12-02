import React, { useEffect, useState } from 'react';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import api from '../api';


function Temper(){
    const [isLoading, setLoading] = useState(false);
    const [classroom, setClassroom] = useState("");
    const [resultFlag , setResultFlag] = useState(false);
    const [temperature, setTemperature] = useState(0);
    const [humid, setHumid] = useState("0%");

    const handleClick = () => setLoading(true);
    const requestHopeTemper = ()=>{
        const hopeTemper = document.getElementById("hopeTemper").value

        api.setTemperatureApi(classroom, hopeTemper)
    }
    useEffect(() => {
        if (isLoading) {
            api.getTemperatureApi(classroom).then(res=>{               
                if(res.data.CODE === 60){
                    setResultFlag(true)
                    setTemperature(res.data.temperature)
                    setHumid(res.data.humid)
                }
                setLoading(false)
            }).catch(()=>setLoading(false));
        }
      }, [isLoading]);

      const Result = (res)=>{
        return (
    
            <>
                <p>강의실 : {classroom}</p>
                <p>온도 : {temperature}</p>
                <p>습도 : {humid}</p><br/>
                        
                <Form.Group className="mb-3">
                    <Form.Label><h5>희망 온도</h5></Form.Label>
                    <Form.Control type="text" placeholder="23..." style={{"width" : "20%"}} id="hopeTemper"/>
                 </Form.Group>
                 <Button
                    variant="outline-primary"
                    onClick={e=>requestHopeTemper()}>
                        희망 온도 설정
                </Button>
            </>
    
        )
    
    
    }

    return (
        <>
        <h4>강의실 온도 조절</h4>
        <Form.Group className="mb-3">
            <Form.Label>강의실</Form.Label>
            <Form.Control type="text" placeholder="D127, DB132..." 
            onChange={e=>setClassroom(e.target.value)} style={{"width" : "50%"}}/>
        </Form.Group>

        <Button
        variant="outline-primary"
        disabled={isLoading}
        onClick={!isLoading ? handleClick : null}>
        {isLoading ? 'Loading…' : '강의실 온도 조회하기'}
        </Button>
        <div id="temperature_result">
            {resultFlag ? <Result /> : null}
        </div>
    </>
    )

}



export default Temper