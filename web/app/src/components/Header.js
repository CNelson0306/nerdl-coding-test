import React from 'react';

function Header() {
  return (
    <header className="site-header">
      <h1>News Website</h1>
      <nav>
        <ul className="nav-list">
          <li><a href="#">Home</a></li>
          <li><a href="#">World</a></li>
          <li><a href="#">Politics</a></li>
          <li><a href="#">Business</a></li>
          <li><a href="#">Technology</a></li>
        </ul>
      </nav>
    </header>
  );
}

export default Header; 