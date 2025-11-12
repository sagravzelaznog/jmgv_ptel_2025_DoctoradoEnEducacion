# Acciones

# Acción: Agregar Módulo de Curso a la Aplicación Existente

**Objetivo:** crear un nuevo archivo html con el módulo de contenido de curso y vincularlo al archivo `index.html` principal.

**Contexto:** Esta acción asume que ya existe el archivo `index.html` con la estructura base (Header, Nav, Main, Footer) y la configuración de Tailwind CSS vía CDN.

---

### Requerimientos de Implementación

**1. Módulo de Contenido (Integración HTML)**

* **Ubicación:** El contenido del nuevo curso debe agregarse como una nueva etiqueta `<section>` dentro de la etiqueta `<main>` del archivo `index.html`.
* **Estructura Semántica:** La sección del curso debe estar claramente estructurada. Se sugiere la siguiente jerarquía:

    ```html
    <section id="curso-nuevo-1" class="py-12 md:py-16">
      <div class="container mx-auto px-4">
        
        <h2 class="text-3xl md:text-4xl font-bold text-emerald-700 mb-4 text-center">
          Nombre del Curso (Ej: Evaluación Formativa)
        </h2>
        <p class="text-lg text-gray-700 mb-8 max-w-3xl mx-auto text-center">
          Objetivo o descripción breve del curso.
        </p>
        
        <div class="space-y-6">
          
          <article class="bg-white p-6 rounded-lg shadow-md border border-gray-200">
            <h3 class="text-2xl font-semibold text-blue-800 mb-3">
              Módulo 1: Fundamentos
            </h3>
            <p class="text-gray-600 mb-4">
              Contenido detallado del módulo 1. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
            </p>
            <ul class="list-disc list-inside text-gray-600 space-y-1">
              <li>Punto clave 1 del módulo.</li>
              <li>Punto clave 2 del módulo.</li>
            </ul>
          </article>
          
          <article class="bg-white p-6 rounded-lg shadow-md border border-gray-200">
            <h3 class="text-2xl font-semibold text-blue-800 mb-3">
              Módulo 2: Técnicas e Instrumentos
            </h3>
            <p class="text-gray-600">
              Contenido detallado del módulo 2. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
            </p>
          </article>
          
          </div>
      </div>
    </section>
    
    ```

**2. Módulo de Estilos (Tailwind CSS)**

* **Sin CSS Adicional:** No se debe agregar ninguna etiqueta `<style>` ni archivos `.css`.
* **Utilidades de Tailwind:** Todo el estilo (márgenes, colores, tipografía, layout) debe implementarse *exclusivamente* con las clases de utilidad de Tailwind CSS.
* **Tema de Color:** Mantener la paleta de colores profesional (azules y esmeraldas) definida en la acción anterior.
* **Responsivo:** Asegurar que el contenido del curso sea completamente responsivo usando los prefijos `sm:`, `md:` y `lg:`.

**3. Módulo de Lógica (JavaScript Modular)**

* **Interactividad Opcional:** Si el nuevo módulo de curso requiere interactividad (ej. un acordeón para mostrar/ocultar el contenido de los módulos), esta lógica debe agregarse al bloque `<script>` existente.
* **Integración:** El nuevo código JS debe:
    * Estar escrito en ES6+ y organizado en funciones claras (ej. `initCourseAccordion()`).
    * Añadirse *dentro* del *listener* `DOMContentLoaded` para asegurar que el DOM esté cargado.
    * No debe interferir con la lógica existente (ej. `initMobileMenu()`).

**4. Requerimiento Específico (Footer)**

* **Inalterado:** El `<footer>` de la página **no debe ser modificado**. Debe mantenerse exactamente como:
    ```html
    <footer class="bg-blue-900 text-gray-200 py-6 mt-auto">
      <div class="container mx-auto px-4 text-center">
        <p>&copy; JMGV-PTEL-2025.Todos los derechos reservados.</p>
      </div>
    </footer>
    ```