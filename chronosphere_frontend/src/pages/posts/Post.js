import React from "react";
import styles from "../../styles/Post.module.css";
import { useCurrentUser } from "../../contexts/CurrentUserContext";
import Card from "react-bootstrap/Card";
import Media from "react-bootstrap/Media";
import OverlayTrigger from "react-bootstrap/OverlayTrigger";
import Tooltip from "react-bootstrap/Tooltip";
import { Link, useHistory } from "react-router-dom";
import Avatar from "../../components/Avatar";
import { axiosRes } from "../../api/axiosDefaults";
import { MoreDropdown } from "../../components/MoreDropdown";

const Post = (props) => {
  const {
    id,
    owner,
    profile_id,
    profile_image,
    comments_count,
    likes_count,
    like_id,
    title,
    content,
    image,
    updated_at,
    created_at,
    postPage,
    setPosts,
    category,
  } = props;

  const currentUser = useCurrentUser();
  const is_owner = currentUser?.username === owner;
  const history = useHistory();

  const handleEdit = () => {
    history.push(`/posts/${id}/edit`);
  };

  const handleDelete = async () => {
    try {
      await axiosRes.delete(`/posts/${id}/`);
      history.goBack();
    } catch (err) {
      // console.log(err);
    }
  };

  const handleLike = async () => {
    try {
      const { data } = await axiosRes.post("/likes/", { post: id });
      setPosts((prevPosts) => ({
        ...prevPosts,
        results: prevPosts.results.map((post) => {
          return post.id === id
            ? { ...post, likes_count: post.likes_count + 1, like_id: data.id }
            : post;
        }),
      }));
    } catch (err) {
      // console.log(err);
    }
  };

  const handleUnlike = async () => {
    try {
      await axiosRes.delete(`/likes/${like_id}/`);
      setPosts((prevPosts) => ({
        ...prevPosts,
        results: prevPosts.results.map((post) => {
          return post.id === id
            ? { ...post, likes_count: post.likes_count - 1, like_id: null }
            : post;
        }),
      }));
    } catch (err) {
      // console.log(err);
    }
  };

  const handleCopyLink = () => {
    const url = `${window.location.origin}/posts/${id}`;
    navigator.clipboard.writeText(url).then(
      () => {
        alert("Post link copied to clipboard!");
      },
      (err) => {
        console.error("Error copying link to clipboard", err);
      }
    );
  };

  return (
    <Card className={styles.Post}>
      <Card.Body>
        <Media className="align-items-center justify-content-between">
          <Link to={`/profiles/${profile_id}`}>
            <Avatar src={profile_image} height={55} />
            {owner}
          </Link>
          <div className="d-flex align-items-center justify-content-end">
            <div className="d-flex flex-column align-items-end mr-3">
              <span>Last update: {updated_at}</span>
              <span className="small text-muted">Created at: {created_at}</span>
            </div>
            {is_owner && postPage && (
              <MoreDropdown
                handleEdit={handleEdit}
                handleDelete={handleDelete}
              />
            )}
          </div>
        </Media>
        <hr />
        {title && <Card.Title className="text-center">{title}</Card.Title>}
        {category && (
          <Card.Subtitle className="mb-2 text-muted text-center">
            Category: {category.name}
          </Card.Subtitle>
        )}
        <hr />
      </Card.Body>
      <Link to={`/posts/${id}/`}>
        <Card.Img src={image} alt={title} />
      </Link>
      <Card.Body>
        {content && <Card.Text>{content}</Card.Text>}
        <div className={styles.PostBar}>
          {is_owner ? (
            <OverlayTrigger
              placement="top"
              overlay={<Tooltip>You cant like your own post!</Tooltip>}
            >
              <i className="far fa-heart" />
            </OverlayTrigger>
          ) : like_id ? (
            <span onClick={handleUnlike}>
              <i className={`fas fa-heart ${styles.Heart}`} />
            </span>
          ) : currentUser ? (
            <span onClick={handleLike}>
              <i className={`far fa-heart ${styles.HeartOutline}`} />
            </span>
          ) : (
            <OverlayTrigger
              placement="top"
              overlay={<Tooltip>Log in to like posts!</Tooltip>}
            >
              <i className="far fa-heart" />
            </OverlayTrigger>
          )}
          {likes_count}
          <OverlayTrigger
            placement="top"
            overlay={<Tooltip>View comments</Tooltip>}
          >
            <span>
              <Link to={`/posts/${id}/`}>
                <i className="far fa-comments" />
                {comments_count}
              </Link>
            </span>
          </OverlayTrigger>
          <OverlayTrigger
            placement="top"
            overlay={<Tooltip>Copy link to clipboard</Tooltip>}
          >
            <span onClick={handleCopyLink}>
              <i className="fa-solid fa-link" style={{ cursor: "pointer" }} />
            </span>
          </OverlayTrigger>
        </div>
      </Card.Body>
    </Card>
  );
};

export default Post;
