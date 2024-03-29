import React, { useState, useEffect, useContext } from "react";
import Container from "react-bootstrap/Container";
import appStyles from "../../App.module.css";
import Asset from "../../components/Asset";
import { axiosReq } from "../../api/axiosDefaults";
import { CurrentUserContext } from "../../contexts/CurrentUserContext";
import { useParams, NavLink } from "react-router-dom";

const UserTopCategories = ({ mobile }) => {
  const [topCategories, setTopCategories] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const currentUser = useContext(CurrentUserContext);
  const { id } = useParams();

  useEffect(() => {
    if (!currentUser || currentUser.profile_id.toString() !== id) {
      setIsLoading(false);
      return;
    }

    const fetchTopCategories = async () => {
      try {
        const { data } = await axiosReq.get(`/user-top-categories/?user_id=${currentUser.profile_id}`);
        const filteredCategories = data.filter(
          (category) =>
            category.category__name !== null && category.category__id !== null
        );
        setTopCategories(filteredCategories);
      } catch (err) {
        console.log(err);
      } finally {
        setIsLoading(false);
      }
    };

    fetchTopCategories();
  }, [currentUser, id]);

  if (!currentUser || currentUser.profile_id.toString() !== id) return null;

  return (
    <Container
      className={`${appStyles.Content} ${
        mobile ? "d-lg-none text-center mb-3" : ""
      }`}
    >
      {isLoading ? (
        <Asset spinner />
      ) : topCategories.length ? (
        <>
          <p>Your Top 5 Categories</p>
          {mobile ? (
            <div className="d-flex flex-wrap justify-content-around">
              {topCategories.map((category) => (
                <NavLink
                  key={category.category__id}
                  to={`/categories/${category.category__id}/posts`}
                  activeClassName="activeLink"
                >
                  <div className="mb-2">{category.category__name}</div>
                </NavLink>
              ))}
            </div>
          ) : (
            topCategories.map((category) => (
              <NavLink
                key={category.category__id}
                to={`/categories/${category.category__id}/posts`}
                activeClassName="activeLink"
              >
                <div className="mb-2">{category.category__name}</div>
              </NavLink>
            ))
          )}
        </>
      ) : (
        <div>You haven&apos;t posted in any categories yet.</div>
      )}
    </Container>
  );
};

export default UserTopCategories;
