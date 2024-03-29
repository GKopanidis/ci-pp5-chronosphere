import React, { useState } from "react";
import { Link } from "react-router-dom";
import Form from "react-bootstrap/Form";
import InputGroup from "react-bootstrap/InputGroup";
import styles from "../../styles/CommentCreateEditForm.module.css";
import Avatar from "../../components/Avatar";
import { axiosRes } from "../../api/axiosDefaults";

const CommentCreateForm = ({
  post,
  setPost,
  setComments,
  profileImage,
  profile_id,
  parentCommentId,
}) => {
  const [content, setContent] = useState("");

  const handleChange = (event) => {
    setContent(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const { data } = await axiosRes.post("/comments/", {
        content,
        post,
        parent: parentCommentId,
      });
  
      setComments((prevComments) => {
        if (parentCommentId) {
          return {
            ...prevComments,
            results: prevComments.results.map((comment) => {
              if (comment.id === parentCommentId) {
                return {
                  ...comment,
                  replies: [data, ...comment.replies],
                  replies_count: comment.replies_count + 1,
                };
              }
              return comment;
            }),
          };
        } else {
          return {
            ...prevComments,
            results: [data, ...prevComments.results],
          };
        }
      });
  
      setPost((prevPost) => ({
        ...prevPost,
        results: [{
          ...prevPost.results[0],
          comments_count: prevPost.results[0].comments_count + 1,
        }],
      }));
  
      setContent("");
    } catch (err) {
      console.log(err);
    }
  };
  

  return (
    <Form className="mt-2" onSubmit={handleSubmit}>
      <Form.Group>
        <InputGroup>
          <Link to={`/profiles/${profile_id}`}>
            <Avatar src={profileImage} />
          </Link>
          <Form.Control
            className={styles.Form}
            as="textarea"
            placeholder="Type your comment here..."
            value={content}
            onChange={handleChange}
            rows={2}
          />
        </InputGroup>
        {parentCommentId && (
          <div style={{ marginTop: "10px", fontSize: "0.9em", color: "#666" }}>
          </div>
        )}
      </Form.Group>
      <button className={`${styles.Button} btn d-block ml-auto`} disabled={!content.trim()} type="submit">
        Post
      </button>
    </Form>
  );
}

export default CommentCreateForm;
