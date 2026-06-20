// Acción al hacer clic en el botón
document.getElementById("btnRegresar").addEventListener("click", function() {
  // Opción 1: Regresar a una URL fija
  window.location.href = "../index.html";

  // Opción 2: Regresar a la página anterior en el historial
  // window.history.back();
});
