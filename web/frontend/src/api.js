import axios from "axios";

const server = "http://localhost:5000"

const classTimeApi = async(classroom, dayweek, period)=>{
    
    let result = await axios.get( server + "/class/time",
    {params : {classroom : classroom, dayweek : dayweek , period : period}}
    );

    return result.data;
}

const attendanceApi = async (classroom) =>{
    let result = await axios.get(server + "/class/attendance",
    {params : {classroom : classroom}});

    return result;
}

const getTemperatureApi = async (classroom) =>{
    let result = await axios.get(server + "/class/temper",
    {params : {classroom : classroom}});

    return result;
}

const setTemperatureApi = async (classroom, hopeTemper) => {
    let result = await axios.post(server + "/class/temper",
    {classroom : classroom, temper : hopeTemper});

    return result
}


const api = {
    classTimeApi : classTimeApi,
    attendanceApi : attendanceApi,
    getTemperatureApi : getTemperatureApi,
    setTemperatureApi : setTemperatureApi
}

export default api;
