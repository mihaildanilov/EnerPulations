
import { useState, useEffect } from 'react';

type DataEntry = {
    hour: string;
    price: number;
    day: string;
};

type ActionEntry = {
    hour: string;
    day: string;
    electricity_price: number;
    action: string;
};

const API_URL = 'http://localhost:3008';
const useOptimizedData = (data: DataEntry[]) => {
    console.log("Data at optimized data", data)
    const [optimizedData, setOptimizedData] = useState<ActionEntry[] | null>(null);
    const [error, setError] = useState<string | null>(null);
    const [loading, setLoading] = useState<boolean>(true);

    useEffect(() => {
        const fetchOptimizedData = async () => {
            try {
                const response = await fetch(`${API_URL}/optimize`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(data),
                });
                const result = await response.json();
                setOptimizedData(result);
            } catch (err: any) { //TODO
                setError(`Error: ${err.message}`);
            } finally {
                setLoading(false);
            }
        };

        fetchOptimizedData();
    }, [data]);

    return { optimizedData, error, loading };
};

export default useOptimizedData;
