import React from "react";
import Spinner from "react-bootstrap/Spinner";
import styles from "../styles/Asset.module.css";

const Asset = ({ spinner, src, message, extraContent }) => {
  return (
    <div className={`${styles.Asset} p-4`}>
      {spinner && <Spinner animation="border" />}
      {src && <img src={src} alt={message} className="mt-3" />}
      {message && <p className="mt-4">{message}</p>}
      {extraContent}
    </div>
  );
};

export default Asset;
