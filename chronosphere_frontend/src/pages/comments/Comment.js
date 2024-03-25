import React, { useState, useEffect } from "react";
import Media from "react-bootstrap/Media";
import { Link } from "react-router-dom";
import Avatar from "../../components/Avatar";
import { MoreDropdown } from "../../components/MoreDropdown";
import CommentEditForm from "./CommentEditForm";
import CommentCreateForm from "./CommentCreateForm";
import styles from "../../styles/Comment.module.css";
import { useCurrentUser } from "../../contexts/CurrentUserContext";
import { axiosRes, axiosReq } from "../../api/axiosDefaults";

const Comment = (props) => {
  const {
    profile_id,
    profile_image,
    owner,
    updated_at,
    content,
    id,
    setPost,
    setComments,
    post,
    replies,
    replies_count,
    is_main_comment,
  } = props;

  const [showEditForm, setShowEditForm] = useState(false);
  const [showReplyForm, setShowReplyForm] = useState(false);
  const [showReplies, setShowReplies] = useState(false);
  const isReply = !!props.parent;
  const [isDeleting, setIsDeleting] = useState(false);
  const [isMounted, setIsMounted] = useState(false);

  useEffect(() => {
    setIsMounted(true);
    return () => setIsMounted(false);
  }, []);

  const currentUser = useCurrentUser();
  const is_owner = currentUser?.username === owner;

  const updateComments = async () => {
    if (!isMounted) return;
    try {
      const { data: updatedComments } = await axiosReq.get(
        `/comments/?post=${post}`
      );
      setComments(updatedComments);
    } catch (err) {
      console.log(err);
    }
  };

  const removeCommentFromState = (id) => {
    setComments((prevComments) => ({
      ...prevComments,
      results: prevComments.results.filter((comment) => comment.id !== id),
    }));

    setPost((prevPost) => ({
      ...prevPost,
      results: prevPost.results.map((result) => ({
        ...result,
        comments_count: result.comments_count - 1,
      })),
    }));
  };

  const handleDelete = async () => {
    setIsDeleting(true);
    try {
      await axiosRes.delete(`/comments/${id}/`);
      if (!isMounted) return;
      removeCommentFromState(id);
      updateComments();
    } catch (err) {
      console.log(err);
    } finally {
      if (isMounted) setIsDeleting(false);
    }
  };

  return (
    <>
      <hr />
      {isDeleting ? (
        <div>Deleting...</div>
      ) : (
        <Media>
          <Link to={`/profiles/${profile_id}`}>
            <Avatar src={profile_image} />
          </Link>
          <Media.Body className="align-self-center ml-2">
            <div className="d-flex justify-content-between align-items-center">
              <div>
                <h6 className={styles.Owner}>{owner}</h6>
                <p className={styles.Date}>{updated_at}</p>
              </div>
              {is_owner && (
                <MoreDropdown
                  handleEdit={() => setShowEditForm(true)}
                  handleDelete={handleDelete}
                />
              )}
            </div>
            {showEditForm ? (
              <CommentEditForm
                id={id}
                profile_id={profile_id}
                content={content}
                profileImage={profile_image}
                setComments={setComments}
                setShowEditForm={setShowEditForm}
              />
            ) : (
              <>
                <p className={styles.Content}>{content}</p>
                <div className={styles.CommentActions}>
                  {!isReply && is_main_comment && currentUser && (
                    <button
                      className={`btn btn-link ${styles.replyButton}`}
                      onClick={() => setShowReplyForm(!showReplyForm)}
                    >
                      {showReplyForm ? "Cancel Reply" : "Reply"}
                    </button>
                  )}
                  {!isReply && replies_count > 0 && (
                    <button
                      className={`btn btn-link ${styles.replyButton}`}
                      onClick={() => setShowReplies(!showReplies)}
                    >
                      {showReplies
                        ? "Hide Replies"
                        : `Show ${replies_count} Replies`}
                    </button>
                  )}
                </div>
                {showReplies && (
                  <div className={styles.Replies}>
                    {replies.map((reply) => (
                      <Comment
                        key={reply.id}
                        {...reply}
                        setPost={setPost}
                        setComments={setComments}
                        post={post}
                        owner={owner}
                        profile_id={profile_id}
                        profile_image={profile_image}
                      />
                    ))}
                  </div>
                )}
              </>
            )}
          </Media.Body>
        </Media>
      )}
      {showReplyForm && !isDeleting && (
        <CommentCreateForm
          post={post}
          setPost={setPost}
          setComments={setComments}
          profileImage={currentUser?.profile_image}
          profile_id={currentUser?.profile_id}
          parentCommentId={id}
        />
      )}
    </>
  );
};

export default Comment;
