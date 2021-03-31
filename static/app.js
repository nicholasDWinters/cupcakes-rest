const list = document.getElementById('cupcakeList');
const form = document.getElementById('form');
const formBtn = document.getElementById('formBtn');

async function getCupcakes() {
    try {
        const res = await axios.get('/api/cupcakes');
        for (let cupcake of res.data.cupcakes) {
            const newItem = document.createElement('li');
            newItem.innerText = `Flavor: ${cupcake.flavor} - Size: ${cupcake.size} - Rating: ${cupcake.rating}`;
            newItem.classList.add('listItem');
            newItem.classList.add('mb-4');

            if (cupcake.image) {
                const newImage = document.createElement('img');
                newImage.src = `${cupcake.image}`;
                newImage.classList.add('cupcakeImg');
                newItem.appendChild(newImage);
            }


            list.appendChild(newItem);
        }
    } catch (e) {
        console.log(e);
    }
}


formBtn.addEventListener('click', async function (e) {
    e.preventDefault();
    const flavor = document.getElementById('flavor').value;
    const size = document.getElementById('size').value;
    const rating = document.getElementById('rating').value;
    const image = document.getElementById('image').value;
    const res = await axios.post('/api/cupcakes', { flavor, size, rating, image });
    const cupcake = res.data.cupcake;

    const newItem = document.createElement('li');
    newItem.innerText = `Flavor: ${cupcake.flavor} - Size: ${cupcake.size} - Rating: ${cupcake.rating}`;
    newItem.classList.add('listItem');
    if (cupcake.image) {
        const newImage = document.createElement('img');
        newImage.src = `${cupcake.image}`;
        newImage.classList.add('cupcakeImg');
        newItem.appendChild(newImage);
    }
    list.appendChild(newItem);

})

getCupcakes();