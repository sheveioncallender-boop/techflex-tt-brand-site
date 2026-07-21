(function () {
  'use strict';

  function ready(fn) {
    if (document.readyState !== 'loading') {
      fn();
    } else {
      document.addEventListener('DOMContentLoaded', fn);
    }
  }

  ready(function () {
    var toggle = document.querySelector('.tfx-menu-toggle');
    var nav = document.querySelector('.tfx-nav');
    if (toggle && nav) {
      toggle.addEventListener('click', function () {
        var isOpen = document.body.classList.toggle('tfx-menu-open');
        toggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
      });
      nav.querySelectorAll('a').forEach(function (link) {
        link.addEventListener('click', function () {
          document.body.classList.remove('tfx-menu-open');
          toggle.setAttribute('aria-expanded', 'false');
        });
      });
      document.addEventListener('keydown', function (event) {
        if (event.key === 'Escape') {
          document.body.classList.remove('tfx-menu-open');
          toggle.setAttribute('aria-expanded', 'false');
        }
      });
    }

    var path = window.location.pathname.replace(/\/$/, '') || '/';
    document.querySelectorAll('.tfx-nav a[data-path]').forEach(function (link) {
      var linkPath = (link.getAttribute('data-path') || '').replace(/\/$/, '') || '/';
      if (path === linkPath) {
        link.classList.add('is-active');
      }
    });
  });
})();
