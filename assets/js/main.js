// Soluciones Tecnológicas — interacción ligera, sin librerías
document.documentElement.classList.add("js");

// Menú móvil
const menuBtn = document.querySelector(".menu-btn");
const nav = document.querySelector(".nav");
if (menuBtn && nav) {
  menuBtn.addEventListener("click", () => {
    const open = nav.classList.toggle("open");
    menuBtn.setAttribute("aria-expanded", String(open));
  });
  nav.addEventListener("click", (e) => {
    if (e.target.closest("a")) {
      nav.classList.remove("open");
      menuBtn.setAttribute("aria-expanded", "false");
    }
  });
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && nav.classList.contains("open")) {
      nav.classList.remove("open");
      menuBtn.setAttribute("aria-expanded", "false");
      menuBtn.focus();
    }
  });
}

// Pestañas de packs
document.querySelectorAll("[role=tablist]").forEach((list) => {
  const tabs = [...list.querySelectorAll("[role=tab]")];
  const select = (tab) => {
    tabs.forEach((t) => {
      const on = t === tab;
      t.setAttribute("aria-selected", String(on));
      t.tabIndex = on ? 0 : -1;
      document.getElementById(t.getAttribute("aria-controls")).hidden = !on;
    });
  };
  tabs.forEach((tab, i) => {
    tab.addEventListener("click", () => select(tab));
    tab.addEventListener("keydown", (e) => {
      const step = e.key === "ArrowRight" ? 1 : e.key === "ArrowLeft" ? -1 : 0;
      if (!step) return;
      const next = tabs[(i + step + tabs.length) % tabs.length];
      select(next);
      next.focus();
    });
  });
});

// Aparición al hacer scroll
const revealables = document.querySelectorAll(".reveal");
if ("IntersectionObserver" in window) {
  const io = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("is-in");
        io.unobserve(entry.target);
      }
    });
  }, { rootMargin: "0px 0px -8% 0px" });
  revealables.forEach((el) => io.observe(el));
} else {
  revealables.forEach((el) => el.classList.add("is-in"));
}

// Formulario: prepara el mensaje y lo abre en WhatsApp (sin servidor)
const form = document.querySelector("#form-contacto");
if (form) {
  const msg = form.querySelector(".form-msg");
  const elegido = new URLSearchParams(location.search).get("servicio");
  const select = form.querySelector("select[name=servicio]");
  if (elegido && select && [...select.options].some((o) => o.value === elegido)) select.value = elegido;
  form.addEventListener("submit", (e) => {
    e.preventDefault();
    const data = new FormData(form);
    const nombre = (data.get("nombre") || "").toString().trim();
    const servicio = select ? select.options[select.selectedIndex].text : "";
    const negocio = (data.get("negocio") || "").toString().trim();
    const mensaje = (data.get("mensaje") || "").toString().trim();
    if (!nombre || !mensaje) {
      msg.textContent = "Escribe tu nombre y cuéntanos un poco lo que necesitas.";
      return;
    }
    if (!data.get("privacidad")) {
      msg.textContent = "Para enviarlo, acepta la política de privacidad.";
      return;
    }
    const numero = form.dataset.whatsapp.replace(/\D/g, "");
    if (!numero) {
      msg.textContent = "Todavía no hay un número de WhatsApp configurado.";
      return;
    }
    msg.textContent = "";
    const texto = [
      `Hola, soy ${nombre}.`,
      negocio ? `Negocio: ${negocio}.` : "",
      `Me interesa: ${servicio}.`,
      mensaje,
    ].filter(Boolean).join("\n");
    window.open(`https://wa.me/${numero}?text=${encodeURIComponent(texto)}`, "_blank", "noopener");
  });
}

// Año del pie
document.querySelectorAll("[data-year]").forEach((el) => { el.textContent = new Date().getFullYear(); });
