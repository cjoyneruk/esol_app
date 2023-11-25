
async function getLocation() {

    const postcode = document.getElementById("postcode").value;

    try {
        const formattedPostcode = postcode.toLowerCase().replace(/\s/g, '');

        const response = await fetch(`https://api.postcodes.io/postcodes/${formattedPostcode}`);
        const data = await response.json();
        // Handle the response data here

        const coords = {
            x: data.result.latitude,
            y: data.result.longitude
        }

        return coords

    } catch (error) {
        // Handle any errors here
        console.error(error);
    }
}


function get_Distance_From_LatLonInKm(x1, y1, x2, y2) {

    Long1 = x1 * (Math.PI/180);
    Lat1 = y1 * (Math.PI/180);
    Long2 = x2 * (Math.PI/180);
    Lat2 = y2 * (Math.PI/180);
    dLat = Lat2 - Lat1;
    dLong = Long2 - Long1;
    
    // Haversine formula
    a = (Math.sin(dLat/2))**2 + Math.cos(Lat1) * Math.cos(Lat2) * (Math.sin(dLong/2))**2;
    c = 2 * Math.atan2 (Math.sqrt(a), Math.sqrt(1-a));
    d = 6371 * c;
    // console.log(d);

    return Math.round(d*100)/100;

}

function filterData(level, distance, userLocationX, userLocationY, data) {
    console.log(data.length);

    // Filter data by level
    const levelFilter = data.filter(function(dataset) {
        return dataset.level == level;
    });

    console.log(levelFilter.length);

    // Add distance to data
    levelFilter.forEach(function(element) {
        element['distance'] = get_Distance_From_LatLonInKm(userLocationX, userLocationY, element.x_loc, element.y_loc);
    });

    // Filter data by distance
    const distanceFilter = levelFilter.filter(function(item) {
        return item.distance < distance;
    });

    // Sort data by distance and time_start
    const sortedData = distanceFilter.sort(function(a, b) {
        if (a.distance === b.distance) {
            return a.time_start.localeCompare(b.time_start);
        }
        return a.distance - b.distance;
    });

    return sortedData;
}

async function fetchData() {

    // Fetch data about classes
    try {
        const response = await fetch('data/entries.json');
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}