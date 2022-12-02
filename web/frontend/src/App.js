import Header from "./components/Header";
import { BrowserRouter, Routes, Route } from 'react-router-dom';

import ClassTime from './components/ClassTime';
import Attendance from "./components/Attendance";
import Temper from "./components/Temper";

function App() {
  return (
    <>
    <BrowserRouter>
      <Header />
      <Routes>
        <Route path="/class/time" element={<ClassTime />}></Route>
        <Route path="/class/attendance" element={<Attendance />}></Route>
        <Route path="class/temper" element={<Temper/>}></Route>
      </Routes>
    </BrowserRouter>
    </>
  );
}

export default App;
