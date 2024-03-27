import React from "react";
import Container from "react-bootstrap/Container";
import styles from "../styles/Footer.module.css";

const Footer = () => {
  return (
    <footer className={styles.footer}>
      <Container>
        <span>&copy; 2024 ChronoSphere. For educational purposes only.</span>
        <div className={styles.links}>
          <a href="https://github.com/GKopanidis" target="_blank" rel="noopener noreferrer">
            <i className="fa-brands fa-github"></i> GitHub
          </a>
          <a href="https://www.linkedin.com/in/georgios-k-308588267/" target="_blank" rel="noopener noreferrer">
            <i className="fa-brands fa-linkedin-in"></i> LinkedIn
          </a>
        </div>
      </Container>
    </footer>
  );
};

export default Footer;