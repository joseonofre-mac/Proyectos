document.addEventListener("DOMContentLoaded", () => {
  
    // Función reutilizable para cargar cualquier CSV e inyectarlo en su respectiva tabla
    function cargarYProcesarCSV(urlCsv, idContenedorTabla) {
      const tablaBody = document.getElementById(idContenedorTabla);
  
      fetch(urlCsv)
        .then(response => {
          if (!response.ok) {
            throw new Error(`No se pudo cargar el archivo: ${urlCsv}`);
          }
          return response.text();
        })
        .then(texto => {
          tablaBody.innerHTML = ""; // Limpiar mensaje de carga
  
          const lineas = texto.split(/\r?\n/);
          
          for (let i = 1; i < lineas.length; i++) {
            const linea = lineas[i].trim();
            if (linea === "") continue;
  
            const [segundo, relevante] = linea.split(",");
  
            // Diseño de los distintivos de color (badge)
            let badgeHTML = "";
            if (relevante === "1") {
              badgeHTML = '<span class="badge bg-success px-2 py-1">1</span>';
            } else {
              badgeHTML = '<span class="badge bg-secondary px-2 py-1">0</span>';
            }
  
            const filaHTML = `
              <tr>
                <td class="fw-mono ps-3">${segundo}</td>
                <td class="text-center">${badgeHTML}</td>
              </tr>
            `;
  
            tablaBody.innerHTML += filaHTML;
          }
        })
        .catch(error => {
          console.error(error);
          tablaBody.innerHTML = `
            <tr>
              <td colspan="2" class="text-center text-danger py-4">
                Error al cargar los datos de este bloque.
              </td>
            </tr>
          `;
        });
    }
  
    // ================= ENRUTAMIENTO DE ARCHIVOS =================
    // 'train.csv' está en la raíz junto al index.html
    cargarYProcesarCSV("../train.csv", "tabla-body-train");
    
    // 'test_resultados.csv' está dentro de la carpeta 'outputs'
    cargarYProcesarCSV("../outputs/test_resultados.csv", "tabla-body-test");
    
});