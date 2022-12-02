import Button from 'react-bootstrap/Button';
import { Link } from 'react-router-dom';

function Header(){

    return (
    <>
        <h1>스마트 강의실</h1><br/>
        <Link to="/class/time">
            <Button variant="primary">시간표 조회하기</Button>{' '}<br /><br/>
        </Link>
        <Link to="/class/temper">
            <Button variant="primary">강의실 온도조절하기</Button>{' '}<br /><br/>
        </Link>
        <Link to="class/attendance">
            <Button variant="primary">실시간 출석체크</Button>{' '}<br /><br/>
        </Link>
        
    </>
    )

}

export default Header