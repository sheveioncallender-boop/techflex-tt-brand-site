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
    var body = document.body;
    var toggle = document.querySelector('.tfx-menu-toggle');
    var nav = document.querySelector('.tfx-nav');
    var dropdown = document.querySelector('.tfx-nav-dropdown');
    var dropdownLink = dropdown ? dropdown.querySelector(':scope > a') : null;

    if (toggle && nav) {
      toggle.addEventListener('click', function () {
        var isOpen = body.classList.toggle('tfx-mobile-menu-open');
        toggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
      });

      nav.querySelectorAll('a').forEach(function (link) {
        link.addEventListener('click', function () {
          if (!link.closest('.tfx-nav-dropdown') || !window.matchMedia('(max-width: 960px)').matches) {
            body.classList.remove('tfx-mobile-menu-open');
            toggle.setAttribute('aria-expanded', 'false');
          }
        });
      });
    }

    if (dropdown && dropdownLink) {
      dropdownLink.addEventListener('click', function (ev) {
        if (window.matchMedia('(max-width: 960px)').matches) {
          ev.preventDefault();
          dropdown.classList.toggle('is-open');
        }
      });
    }

    var path = window.location.pathname.replace(/\/$/, '') || '/';
    document.querySelectorAll('.tfx-nav a[data-path]').forEach(function (link) {
      var linkPath = (link.getAttribute('data-path') || '').replace(/\/$/, '') || '/';
      if (linkPath === path || (linkPath !== '/' && path.indexOf(linkPath) === 0)) {
        link.classList.add('is-active');
      }
    });
  });
})();
