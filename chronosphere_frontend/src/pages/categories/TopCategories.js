import React, { useState, useEffect } from "react";
import Container from "react-bootstrap/Container";
import appStyles from "../../App.module.css";
import Asset from "../../components/Asset";
import { axiosReq } from "../../api/axiosDefaults";
import { Link } from "react-router-dom"; // Importiere Link

const TopCategories = ({ mobile }) => {
  const [topCategories, setTopCategories] = useState([]);

  useEffect(() => {
    const fetchTopCategories = async () => {
      try {
        const { data } = await axiosReq.get("/top-categories/");
        setTopCategories(data);
      } catch (err) {
        console.log(err);
      }
    };

    fetchTopCategories();
  }, []);

  return (
    <Container
      className={`${appStyles.Content} ${mobile && "d-lg-none text-center mb-3"}`}
    >
      {topCategories.length ? (
        <>
          <p>Top 5 Categories</p>
          {mobile ? (
            <div className="d-flex flex-wrap justify-content-around">
              {topCategories.map((category) => (
                <Link key={category.id} to={`/categories/${category.id}/posts`}>
                  {category.name}
                </Link>
              ))}
            </div>
          ) : (
            topCategories.map((category) => (
              <div key={category.id} className="mb-2">
                <Link to={`/categories/${category.id}/posts`}>
                  {category.name}
                </Link>
              </div>
            ))
          )}
        </>
      ) : (
        <Asset spinner />
      )}
    </Container>
  );
};

export default TopCategories;
