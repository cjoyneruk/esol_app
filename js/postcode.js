
async function getCoords() {

    console.log('Hello')
    const postcode = document.getElementById("postcode").value;

    try {
        const formattedPostcode = postcode.toLowerCase().replace(/\s/g, '');

        // console.log('Postcode', formattedPostcode);

        const response = await fetch(`https://api.postcodes.io/postcodes/${formattedPostcode}`);
        const data = await response.json();
        // Handle the response data here

        const coords = {
            x: data.result.longitude,
            y: data.result.latitude
        }

        console.log(coords);
        return coords

    } catch (error) {
        // Handle any errors here
        console.error(error);
    }
}
