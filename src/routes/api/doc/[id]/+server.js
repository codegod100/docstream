import { json, text } from '@sveltejs/kit';
import fs from 'fs'
/** @type {import('./$types').RequestHandler} */
export async function POST({ request, params, url }) {
    const data = await request.text();
    console.log(url)
    console.log("got data", data)
    fs.writeFileSync(`${params.id}.json`, data)
    return json("OK")
}

export async function GET({ request, params }) {
    let data
    try {
        data = fs.readFileSync(`${params.id}.json`, { encoding: "utf-8" })

    } catch (e) {
        console.log(e)
        let url = new URL(request.url);
        let author = url.searchParams.get('author');
        data = `[{"author":"${author}", "blips":[], "html":"edit me"}]`
    }
    return json(data)
}