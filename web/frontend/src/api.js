import axios from "axios";

const classTimeApi = async(classroom, dayweek, period)=>{
    
    let result = await axios.get("http://localhost:5000/",
    {params : {classroom : classroom, dayweek : dayweek , period : period}}
    );

    return result.data;
}



const api = {
    classTimeApi : classTimeApi
}

export default api;
