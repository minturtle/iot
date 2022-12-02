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
                console.log(res);
                setLoading(false);
            }).catch(()=>setLoading(true));
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
        </>

    )
}

export default Attendance