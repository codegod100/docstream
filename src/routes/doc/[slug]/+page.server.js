
/** @type {import('./$types').PageLoad} */
export async function load({ fetch, params, url }) {
    let slug = params.slug
    let endpoint = `http://localhost:5000/doc/${slug}`
    let author = url.searchParams.get('author') || generateUsername()
    let data = await fetch(`${endpoint}?author=${author}`)
    let json = await data.json()

    return {
        json, slug, author
    }
}



