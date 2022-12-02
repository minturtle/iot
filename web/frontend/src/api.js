import axios from "axios";

const classTimeApi = async(classroom, dayweek, period)=>{
    
    return axios.get("http://localhost:5000/",
    {params : {classroom : classroom, dayweek : dayweek , period : period}}
    );
}



const api = {
    classTimeApi : classTimeApi
}

export default api;
