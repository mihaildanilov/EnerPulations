import { useState, useEffect } from 'react';
const API_URL = process.env.NEXT_PUBLIC_API_URL;

const useFetchData = () => {
  const [data, setData] = useState();
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState<boolean>(true);

  useEffect(() => {
    const fetchData = async () => {
      setLoading(true); // Ensure loading is true at the start of a fetch operation
      try {
        // const response = await fetch(`http://localhost:3008/fetch-prices`, {
        const response = await fetch(`${API_URL}/fetch-prices`, {
          method: 'GET',
          headers: { 'Content-Type': 'application/json' },
        });
        if (!response.ok) throw new Error('Failed to fetch data');
        const result = await response.json();
        setData(result);
      } catch (err) {
        setError(err instanceof Error ? err.message : 'An unknown error occurred');
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []); // Removed data from dependencies to prevent re-fetching

  return { data, error, loading };
};

export default useFetchData;
