const Navbar = () => {
  const links = [
    {
      label: "Home",
      href: "/"
    },
  ]
  return (
    <nav class="navbar navbar-expand-sm navbar-primary bg-primary px-3">
      <a class="navbar-brand text-light" href="#">Logo</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          {links.map(link => (
            <li class="nav-item">
              <a className="nav-link text-light" href={link.href}>{link.label}</a>
            </li>
          ))}
        </ul>
      </div>
    </nav>
  );
};

export default Navbar;