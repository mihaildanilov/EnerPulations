
import { useState, useEffect } from 'react';

type DataEntry = {
    hour: string;
    price: string;
    day: string;
};

type ActionEntry = {
    hour: string;
    day: string;
    electricity_price: number;
    action: string;
};

const useOptimizedData = (data: DataEntry[]) => {
    const [optimizedData, setOptimizedData] = useState<ActionEntry[] | null>(null);
    const [error, setError] = useState<string | null>(null);
    const [loading, setLoading] = useState<boolean>(true);

    useEffect(() => {
        const fetchOptimizedData = async () => {
            try {
                const response = await fetch('http://localhost:3009/optimize', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ data }),
                });
                const result = await response.json();
                setOptimizedData(result);
            } catch (err) {
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
