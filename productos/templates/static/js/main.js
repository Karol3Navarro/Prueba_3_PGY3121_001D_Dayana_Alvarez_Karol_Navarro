const btnCart = document.querySelector('.container-cart-icon');
const containerCartProducts = document.querySelector(
	'.container-cart-products'
);

btnCart.addEventListener('click', () => {
	containerCartProducts.classList.toggle('hidden-cart');
});

/* ========================= */
const cartInfo = document.querySelector('.cart-product');
const rowProduct = document.querySelector('.row-product');

// Lista de todos los contenedores de productos
const productsList = document.querySelector('.container-items');

// Variable de arreglos de Productos
let allProducts = [];

const valorTotal = document.querySelector('.total-pagar');

const countProducts = document.querySelector('#contador-productos');

const cartEmpty = document.querySelector('.cart-empty');
const cartTotal = document.querySelector('.cart-total');

productsList.addEventListener('click', e => {
	if (e.target.classList.contains('btn-add-cart')) {
		const product = e.target.parentElement;

		const infoProduct = {
			quantity: 1,
			title: product.querySelector('h5').textContent,
			price: product.querySelector('p').textContent,
		};

		const exits = allProducts.some(
			product => product.title === infoProduct.title
		);

		if (exits) {
			const products = allProducts.map(product => {
				if (product.title === infoProduct.title) {
					product.quantity++;
					return product;
				} else {
					return product;
				}
			});
			allProducts = [...products];
		} else {
			allProducts = [...allProducts, infoProduct];
		}

		showHTML();
	}
});

rowProduct.addEventListener('click', e => {
	if (e.target.classList.contains('icon-close')) {
		const product = e.target.parentElement;
		const title = product.querySelector('p').textContent;

		allProducts = allProducts.filter(
			product => product.title !== title
		);

		console.log(allProducts);

		showHTML();
	}
});

// Funcion para mostrar  HTML
const showHTML = () => {
	if (!allProducts.length) {
		cartEmpty.classList.remove('hidden');
		rowProduct.classList.add('hidden');
		cartTotal.classList.add('hidden');
	} else {
		cartEmpty.classList.add('hidden');
		rowProduct.classList.remove('hidden');
		cartTotal.classList.remove('hidden');
	}

	// Limpiar HTML
	rowProduct.innerHTML = '';

	let total = 0;
	let totalOfProducts = 0;

	allProducts.forEach(product => {
		const containerProduct = document.createElement('div');
		containerProduct.classList.add('cart-product');

		containerProduct.innerHTML = `
            <div class="info-cart-product">
                <span class="cantidad-producto-carrito">${product.quantity}</span>
                <p class="titulo-producto-carrito">${product.title}</p>
                <span class="precio-producto-carrito">${product.price}</span>
            </div>
            <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="1.5"
                stroke="currentColor"
                class="icon-close"
            >
                <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M6 18L18 6M6 6l12 12"
                />
            </svg>
        `;

		rowProduct.append(containerProduct);

		total =
			total + parseInt(product.quantity * product.price.slice(1));
		totalOfProducts = totalOfProducts + product.quantity;
	});

	valorTotal.innerText = `$${total}`;
	countProducts.innerText = totalOfProducts;
};
/*Alertaaa*/ 
function Confirmar(){
    var retVal = confirm("¿Seguro desea continuar?");
    if( retVal == true ){
        alert ("OK, REGISTRO ALMACENADO");
        return true;
    }else{
        alert("NO SE GUARDÓ EL REGISTRO");
        return false;
    }
}

//Filtro por nombre

var ordenAscendente = true;

function ordenarPorPrecio() {
    console.log("Función ordenarPorPrecio() llamada");
    var container = document.getElementById("product-container");
    var products = Array.from(container.querySelectorAll('.Ccard'));

    // Ordenar productos por precio
    products.sort(function(a, b) {
        var priceA = parseFloat(a.querySelector('.price').textContent.replace('$', '').replace(',', ''));
        var priceB = parseFloat(b.querySelector('.price').textContent.replace('$', '').replace(',', ''));
        
        // Alternar entre orden ascendente y descendente
        if (ordenAscendente) {
            return priceA - priceB;
        } else {
            return priceB - priceA;
        }
    });

    // Limpiar el contenedor de productos y agregar los productos ordenados
    container.innerHTML = '';
    products.forEach(function(product) {
        container.appendChild(product);
    });

    // Cambiar la dirección del orden para la próxima vez que se llame a la función
    ordenAscendente = !ordenAscendente;
}
//Filtro alfabeticamente
function ordenarAlfabeticamente() {
    console.log("Función ordenarAlfabeticamente() llamada");
    var container = document.getElementById("product-container");
    var products = Array.from(container.querySelectorAll('.Ccard'));

    // Ordenar productos alfabéticamente por título
    products.sort(function(a, b) {
        var titleA = a.querySelector('.card-title').textContent.toLowerCase();
        var titleB = b.querySelector('.card-title').textContent.toLowerCase();

        if (ordenAscendente) {
            if (titleA < titleB) return -1;
            if (titleA > titleB) return 1;
            return 0;
        } else {
            if (titleA > titleB) return -1;
            if (titleA < titleB) return 1;
            return 0;
        }
    });

    // Limpiar el contenedor de productos y agregar los productos ordenados
    container.innerHTML = '';
    products.forEach(function(product) {
        container.appendChild(product);
    });

    // Cambiar la dirección del orden para la próxima vez que se llame a la función
    ordenAscendente = !ordenAscendente;
}
// icono de cantidad de productos
document.addEventListener('DOMContentLoaded', function() {
    // Obtener todos los botones "Añadir al carrito"
    const addToCartButtons = document.querySelectorAll('.btn-add-cart');

    // Array para almacenar los productos en el carrito
    let carrito = [];

    // Función para manejar el clic en el botón "Añadir al carrito"
    function addToCart(event) {
        // Obtener el contenedor del producto
        const productContainer = event.target.closest('.Ccard');
        
        // Obtener información del producto
        const productName = productContainer.querySelector('.card-title').textContent;
        const productPrice = productContainer.querySelector('.price').textContent;

        // Crear objeto de producto
        const product = {
            name: productName,
            price: productPrice
        };

        // Agregar producto al carrito
        carrito.push(product);

        // Actualizar el número de productos en el carrito
        actualizarNumeroProductos(carrito.length);
    }

    // Agregar evento de clic a cada botón "Añadir al carrito"
    addToCartButtons.forEach(button => {
        button.addEventListener('click', addToCart);
    });

    // Función para actualizar el número de productos en el carrito
    function actualizarNumeroProductos(cantidad) {
        const cantidadProductosElemento = document.getElementById("cantidad-productos");
        cantidadProductosElemento.textContent = cantidad.toString();
    }
});
function buscarProducto2() {
    var input = document.querySelector('.search-input');
    var filter = input.value.toLowerCase();
    var cards = document.querySelectorAll('.Ccard');

    cards.forEach(function(card) {
        var title = card.querySelector('.card-title').textContent.toLowerCase();
        if (title.indexOf(filter) > -1) {
            card.style.display = '';
        } else {
            card.style.display = 'none';
        }
    });
}





//Funcion de Login
function login(){
	var usuario=document.getElementById("username").value;
	var clave=document.getElementById("password").value;

	if(usuario== "popsipatitas@gmail.com" &&clave=="1234"){
		alert("Usuario correcto");
	}else{
		alert("Usuario incorrecto");
	}
};