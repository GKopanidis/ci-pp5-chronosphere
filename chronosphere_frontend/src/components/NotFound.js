import React from "react";
import { Link } from "react-router-dom";
import NoResults from "../assets/no-results.png";
import styles from "../styles/NotFound.module.css";
import Asset from "./Asset";

const NotFound = () => {
  const extraContent = (
    <div className={NotFound.linkToHome}>
      <Link to="/">Click here to go back to Home Page</Link>
    </div>
  );

  return (
    <div className={styles.NotFound}>
      <Asset
        src={NoResults}
        message="Sorry, the page you're looking for doesn't exist"
        extraContent={extraContent}
      />
    </div>
  );
};

export default NotFound;
