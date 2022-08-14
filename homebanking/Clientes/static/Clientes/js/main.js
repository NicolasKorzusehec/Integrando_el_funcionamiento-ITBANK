//urls
const cuenta_url = 'http://127.0.0.1:5500/src/data/user-account.json' //datos usuario
const cotizacion_url = 'https://www.dolarsi.com/api/api.php?type=valoresprincipales'; //API para las cotizaciones

//identificadores DOM
const linkProfile = document.querySelector('#profile span');
const sectionCotizaciones = document.querySelector('#cotizacion-dolar .container .row');
const sectionSaldo = document.querySelector('#saldo-cuenta .card');
const chkOcultarDatos = document.querySelector('#ocultar-datos');

// objetos que almacenen datos
var cuenta; //aca se almacenara el fetch de la cuenta
var cotizaciones; //aca se almacena el fetch del dolar

//Trae los datos de usuario e invoca sus impresiones relacionadas
async function fetchCuenta() {
   const response = await fetch(cuenta_url);
   cuenta = await response.json();
   displayProfile();
   displaySaldoCuenta();
};

//Imprime miniatura usuario
function displayProfile() {
   linkProfile.innerHTML = `
	${cuenta.nombre} ${cuenta.apellido}`;
};

//Imprime section-saldo
function displaySaldoCuenta() {
    sectionSaldo.innerHTML = `
    <div class="card-header d-flex align-items-center">
      <span class="me-auto fs-4 fw-semibold">Caja de Ahorro</span>
      <span class="text-muted">Último acceso: ${cuenta.ultimo_acceso.fecha} ${cuenta.ultimo_acceso.hora} hs</span>
    </div>
    <div class="card-body">
      <p class="card-text mb-3">
         <span class="fw-semibold">${cuenta.tipo_cuenta}</span>
         &nbsp;
         <span>${!chkOcultarDatos.checked ? cuenta.id_cuenta : '***-******/*'}</span>
      </p>
      <h4 class="card-text mb-2">$ <span class="fw-bold">${!chkOcultarDatos.checked ? cuenta.saldo.ars : '***'}</span></h4>

      <h5 class="card-text text-success mb-3">U$S <span class="fw-bold">${!chkOcultarDatos.checked ? cuenta.saldo.usd : '***'}</span></h5>

      <p class="card-text">CBU: <span class="fw-semibold">${!chkOcultarDatos.checked ? cuenta.cbu : '******'}</span></p>

      <p class="card-text">Alias: <span class="fw-semibold">${!chkOcultarDatos.checked ? cuenta.alias : '******'}</span></p>
    </div>`;
};

//Trae los datos de cotizaciones e invoca sus impresiones relacionadas
async function fetchCotizaciones() {
   const response = await fetch(cotizacion_url);
   cotizaciones = await response.json();
   displayCotizacionDolar();
};

//Función que agrega dinámicamente a la página contenido de cotizaciones
function displayCotizacionDolar() {
   /*Pendiente agregar en formato
   <p>Variacion: ${caso.casa.variacion}</p>*/
   sectionCotizaciones.innerHTML = '';
   for (let i = 0; i < cotizaciones.length-3; i++) {
      sectionCotizaciones.innerHTML += `
      <div class="col-12 col-sm-6 col-md-4">
         <div class="card text-center m-2">
            <div class="card-header">
               <i class="fa-solid fa-money-bill-wave" style="color:green"></i> 
               ${cotizaciones[i].casa.nombre.toUpperCase()}
            </div>
            <div class="row card-body">
               <div class="col-6 col-sm-12 col-xl-6">
                     <p class="card-text">COMPRA</p>
                     <h3 class="card-title">${cotizaciones[i].casa.compra}</h3>
               </div>
               <div class="col-6 col-sm-12 col-xl-6">
                     <p class="card-text">VENTA</p>
                     <h3 class="card-title">${cotizaciones[i].casa.venta}</h3>
               </div>
            </div>
            <div class="card-footer text-muted">
            ACTUALIZADO: ${cotizaciones[cotizaciones.length-1].casa.fecha} ${cotizaciones[cotizaciones.length-1].casa.recorrido}
            </div>
         </div>
      </div>`
    
   }
      /*pendiente:
      let correccionDecimal = caso.casa.compra;
       console.log(typeof correccionDecimal !== 'string');
       //tratando corregir que solo hayan 2 decimales, no hubo cambios
       if (typeof correccionDecimal !== 'string') {
           correccionDecimal = Number(caso.casa.compra).toFixed(2);
       }*/
};

//Función que agrega la funcionalidad de descargar el pdf del ID seleccionado. Utiliza la librería HTML2PDF
//HTML2PDF: junta las 2 librerías html2canvas y jsPDF
function descargarPdf() {
   const descargar = document.getElementById('cotizacion-dolar');

   html2pdf()
       .set({
           margin: 1,
           filename: 'Cotizaciones.pdf',
           image: {
               type: 'jpeg',
               quality: 0.9,
           },
           //Configuraciones del estilo del pdf (para mantener el original del HTML). Librería html2canvas
           html2canvas: {
               scale: 7,
               letterRendering: true,
           },
           //Configuraciones del propio pdf. Librería jsPDF
           jsPDF: {
               unit: 'cm',
               format: 'a4',
               orientation: 'portrait',
           },
       })
       .from(descargar)
       .save()
       .finally();
};

function actualizarPagina() {
   //fetchCuenta();
   fetchCotizaciones();
};

document.addEventListener('DOMContentLoaded', actualizarPagina, false);
