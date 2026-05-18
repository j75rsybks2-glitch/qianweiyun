/**
 * 扬州千味韵食品 - 企业主页交互
 */
(function () {
  "use strict";

  const header = document.getElementById("header");
  const navToggle = document.getElementById("navToggle");
  const navMenu = document.getElementById("navMenu");
  const navLinks = document.querySelectorAll(".nav-link");
  const contactForm = document.getElementById("contactForm");
  const formNote = document.getElementById("formNote");

  // 滚动时导航栏样式
  function onScroll() {
    if (window.scrollY > 50) {
      header.classList.add("scrolled");
    } else {
      header.classList.remove("scrolled");
    }
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  // 移动端菜单
  navToggle.addEventListener("click", () => {
    const open = navMenu.classList.toggle("open");
    navToggle.setAttribute("aria-expanded", open);
    navToggle.setAttribute("aria-label", open ? "关闭菜单" : "打开菜单");
  });

  navLinks.forEach((link) => {
    link.addEventListener("click", () => {
      navMenu.classList.remove("open");
      navToggle.setAttribute("aria-expanded", "false");
    });
  });

  // 数字滚动动画
  function animateCount(el) {
    const target = parseInt(el.dataset.count, 10);
    const duration = 1500;
    const start = performance.now();
    function step(now) {
      const progress = Math.min((now - start) / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3);
      el.textContent = Math.floor(eased * target);
      if (progress < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }

  const statObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          animateCount(entry.target);
          statObserver.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.5 }
  );
  document.querySelectorAll(".stat-num").forEach((el) => statObserver.observe(el));

  // 产品 Tab 切换
  const tabs = document.querySelectorAll(".product-tab");
  const panels = document.querySelectorAll(".product-panel");

  tabs.forEach((tab) => {
    tab.addEventListener("click", () => {
      const id = tab.dataset.tab;
      tabs.forEach((t) => {
        t.classList.remove("active");
        t.setAttribute("aria-selected", "false");
      });
      tab.classList.add("active");
      tab.setAttribute("aria-selected", "true");

      panels.forEach((panel) => {
        const match = panel.id === `panel-${id}`;
        panel.hidden = !match;
        panel.classList.toggle("active", match);
      });
    });
  });

  // 滚动渐入
  const fadeEls = document.querySelectorAll(
    ".section-header, .about-grid, .timeline-item, .products-hot, .product-hot-card, .product-showcase, .news-card, .partner-logo, .metric-card, .contact-grid"
  );
  fadeEls.forEach((el) => el.classList.add("fade-in"));

  const fadeObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("visible");
          fadeObserver.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.1, rootMargin: "0px 0px -40px 0px" }
  );
  fadeEls.forEach((el) => fadeObserver.observe(el));

  // 联系表单
  contactForm.addEventListener("submit", (e) => {
    e.preventDefault();
    formNote.className = "form-note";
    formNote.textContent = "";

    const name = document.getElementById("name").value.trim();
    const phone = document.getElementById("phone").value.trim();
    const message = document.getElementById("message").value.trim();

    if (!name || !phone || !message) {
      formNote.className = "form-note error";
      formNote.textContent = "请填写所有必填项。";
      return;
    }

    const phoneRe = /^1[3-9]\d{9}$|^0\d{2,3}-?\d{7,8}$/;
    if (!phoneRe.test(phone.replace(/\s/g, ""))) {
      formNote.className = "form-note error";
      formNote.textContent = "请输入有效的电话号码。";
      return;
    }

    formNote.className = "form-note success";
    formNote.textContent = "感谢您的留言！我们会尽快与您联系。";
    contactForm.reset();
  });
})();
