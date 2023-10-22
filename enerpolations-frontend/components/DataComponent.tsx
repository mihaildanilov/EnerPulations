// src/components/DataComponent.tsx
import React, { useEffect, useState } from 'react';
import { fetchData } from '../services/scraperHook';
import useOptimizedData from '../services/useOptimizedData';

type ActionEntry = {
    hour: string;
    day: string;
    electricity_price: number;
    action: string;
};

const DataComponent: React.FC = () => {
    const [data, setData] = useState(null);


    useEffect(() => {
        const getPriceData = async () => {
            try {
                const fetchedData = await fetchData();
                setData(fetchedData);
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };
        getPriceData();
        
    }, []);

    const { optimizedData: commands, error: optimizeError, loading: optimizeLoading } = useOptimizedData(data!);
    return (
        <div>
            {data ? (
                <pre>{JSON.stringify(data, null, 2)}</pre>
            ) : (
                <p>Loading data...</p>
            )}
            {commands ? (
                <pre>{JSON.stringify(commands, null, 2)}</pre>
            ) : optimizeLoading ? (
                <p>Optimizing data...</p>
            ) : optimizeError ? (
                <p>Error optimizing data: {optimizeError}</p>
            ) : null}
        </div>
    );
};

export default DataComponent;
