window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true,
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex",
  },
};

document$.subscribe(() => {
  // The page title shown in the header after scrolling is plain text; let MathJax
  // typeset any inline math it contains (e.g. in gallery page titles).
  document
    .querySelectorAll('[data-md-component="header-title"] .md-header__topic .md-ellipsis')
    .forEach((el) => {
      if (el.textContent.includes("\\(")) el.classList.add("arithmatex");
    });
  MathJax.typesetPromise();
});
