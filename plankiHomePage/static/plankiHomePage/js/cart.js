let cart = []

function addToCart(article) {
    if (localStorage.getItem('cart')) {
        cart = JSON.parse(localStorage.getItem('cart'));
    }

    const existingItem = cart.find(i => i.article === article);
    if (existingItem) {
        existingItem.quantity += 1;
    } else {
        cart.push({ article: article, quantity: 1 });
    }

    localStorage.setItem('cart', JSON.stringify(cart))
}

function removeFromCart(article) {
    if (localStorage.getItem('cart')) {
        cart = JSON.parse(localStorage.getItem('cart'));
    }

    const existingItem = cart.find(i => i.article === article);
    if (existingItem) {
        existingItem.quantity -= 1;
        if (existingItem.quantity <= 0) {
            index = cart.indexOf(existingItem);
            cart.splice(index, 1);
        }
    }
    localStorage.setItem('cart', JSON.stringify(cart));
}

function clearCart() {
    cart = [];
    localStorage.clear();
}




// function getCookie(name) {
//     let cookieValue = null;
//     if (document.cookie && document.cookie !== '') {
//         const cookies = document.cookie.split(';');
//         for (let i = 0; i < cookies.length; i++) {
//             const cookie = cookies[i].trim();
//             // Does this cookie string begin with the name we want?
//             if (cookie.substring(0, name.length + 1) === (name + '=')) {
//                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                 break;
//             }
//         }
//     }
//     return cookieValue;
// }
// const csrftoken = getCookie('csrftoken');

let xhr = new XMLHttpRequest();
xhr.open("POST", "/sendCart/");
xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
xhr.send(JSON.stringify({ "key": "value" }));
