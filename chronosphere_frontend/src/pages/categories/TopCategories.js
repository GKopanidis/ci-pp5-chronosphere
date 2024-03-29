import React, { useState, useEffect } from "react";
import Container from "react-bootstrap/Container";
import appStyles from "../../App.module.css";
import Asset from "../../components/Asset";
import { axiosReq } from "../../api/axiosDefaults";
import { NavLink } from "react-router-dom";

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
      className={`${appStyles.Content} ${
        mobile && "d-lg-none text-center mb-3"
      }`}
    >
      <p>Top 5 Categories</p>
      {mobile ? (
        <div className="d-flex flex-wrap justify-content-around">
          <NavLink activeStyle={{ color: "#c90f0f" }} exact to="/">
            All Categories
          </NavLink>
          {topCategories.map((category) => (
            <NavLink
              key={category.id}
              to={`/categories/${category.id}/posts`}
              activeClassName="activeLink"
            >
              {category.name}
            </NavLink>
          ))}
        </div>
      ) : (
        <>
          <div className="mb-2">
            <NavLink activeStyle={{ color: "#c90f0f" }} exact to="/">
              All Categories
            </NavLink>
          </div>
          {topCategories.length ? (
            topCategories.map((category) => (
              <div key={category.id} className="mb-2">
                <NavLink
                  activeStyle={{ color: "#c90f0f" }}
                  to={`/categories/${category.id}/posts`}
                >
                  {category.name}
                </NavLink>
              </div>
            ))
          ) : (
            <Asset spinner />
          )}
        </>
      )}
    </Container>
  );
};

export default TopCategories;
