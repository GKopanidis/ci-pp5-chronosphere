import React from "react";
import { Navbar, Nav, Container } from "react-bootstrap";
import logo from "../assets/chronosphere_logo.png";

const NavBar = () => {
  return (
    <Navbar expand="md" fixed="top">
      <Container>
        <Navbar.Brand>
          <img src={logo} alt="logo" height="60" />
        </Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="ml-auto text-left">
            <Nav.Link>
              <i className="fas fa-house-chimney"></i>Home
            </Nav.Link>
            <Nav.Link>
              <i className="fa-solid fa-right-to-bracket"></i>Sign In
            </Nav.Link>
            <Nav.Link>
              <i className="fa-solid fa-user-plus"></i>Sign Up
            </Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
};

export default NavBar;
