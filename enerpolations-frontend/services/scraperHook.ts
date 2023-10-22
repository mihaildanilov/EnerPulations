// src/services/api.ts
import axios from 'axios';

const API_URL = 'http://localhost:3008';

export const fetchData = async () => {
    try {
        const response = await axios.get(`${API_URL}/fetch-prices`);
        console.log("Response",response)
        return response.data;
    } catch (error) {
        console.error('Error fetching data:', error);
        throw error;
    }
};
