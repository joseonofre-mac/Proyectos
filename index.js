// Definimos las rutas
const routes = {
  pagina1: "PTAR/inicio.html",
  pagina2: "pagina2.html",
  pagina3: "pagina3.html"
  pagina4: "pagina4.html"
  pagina5: "RelevanciaVideos/inicio.html"
};

function initCardEvents() {
  document.querySelectorAll('.tarjeta').forEach(card => {
    const routeKey = card.getAttribute('data-route');
    const url = routes[routeKey];

    // Evento doble click en escritorio
    card.addEventListener('dblclick', () => {
      window.location.href = url;
    });

    // Simulación de doble tap en móviles
    let lastTap = 0;
    card.addEventListener('touchstart', () => {
      const currentTime = new Date().getTime();
      const tapLength = currentTime - lastTap;
      if (tapLength < 300 && tapLength > 0) {
        // Doble tap detectado
        window.location.href = url;
      }
      lastTap = currentTime;
    });
  });
}

document.addEventListener('DOMContentLoaded', initCardEvents);
