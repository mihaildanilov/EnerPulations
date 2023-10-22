import express from 'express';
import axios from 'axios';
import cheerio from 'cheerio';
import { optimizeActionPlan } from './optimizer';
const app = express();
const PORT = 3008;

interface DataObject {
    hour: string;
    price: number;
    day: string;
}

interface ActionEntry {
    hour: string;
    day: string;
    electricity_price: number;
    action: string;
}

app.use((req, res, next) => {
    res.header('Access-Control-Allow-Origin', 'http://localhost:3000');
    res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept');
    next();
});

app.get('/fetch-prices', async (req, res) => {
    try {
        const url = 'https://www.e-cena.lv/';
        const response = await axios.get(url);
        const $ = cheerio.load(response.data);
        const tables = $('table');
        const data: DataObject[] = [];
        tables.each((i, table) => {
            const rows = $(table).find('tr').slice(1);  // Skipping header
            const day = $('h4').eq(i).text().trim();
            rows.each((j, row) => {
                const hour = $(row).find('td').eq(1).text().trim();
                const price = parseFloat($(row).find('td').eq(0).text().trim())
                data.push({ hour, price, day });
            });
        });
        res.json(data);
    } catch (error) {
        console.error(error);
        res.status(500).send('Server Error');
    }
});

app.post('/optimize', (req, res) => {
    const data: DataObject[] = req.body.data;
    console.log("Data sent to optimizer",data)
    if (!Array.isArray(data) || data.length === 0) {
        res.status(400).send('Invalid data');
        return;
    }
    const optimizedPlan: ActionEntry[] = optimizeActionPlan(data);
    res.json(optimizedPlan);
});


app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
