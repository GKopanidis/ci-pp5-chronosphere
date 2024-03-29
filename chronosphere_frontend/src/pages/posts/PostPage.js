import React, { useEffect, useState } from "react";
import Col from "react-bootstrap/Col";
import Row from "react-bootstrap/Row";
import Container from "react-bootstrap/Container";
import appStyles from "../../App.module.css";
import { useParams } from "react-router-dom";
import { axiosReq } from "../../api/axiosDefaults";
import Post from "./Post";
import Comment from "../comments/Comment";
import CommentCreateForm from "../comments/CommentCreateForm";
import { useCurrentUser } from "../../contexts/CurrentUserContext";
import InfiniteScroll from "react-infinite-scroll-component";
import Asset from "../../components/Asset";
import { fetchMoreData } from "../../utils/utils";
import PopularProfiles from "../profiles/PopularProfiles";
import NotFound from "../../components/NotFound";

const PostPage = () => {
  const { id } = useParams();
  const [post, setPost] = useState({ results: [] });
  const currentUser = useCurrentUser();
  const profile_image = currentUser?.profile_image;
  const [comments, setComments] = useState({ results: [] });
  const [error, setError] = useState(false);

  useEffect(() => {
    const handleMount = async () => {
      try {
        const [{ data: post }, { data: comments }] = await Promise.all([
          axiosReq.get(`/posts/${id}/`),
          axiosReq.get(`/comments/?post=${id}`),
        ]);
        setPost({ results: [post] });
        setComments(comments);
        setError(false);
      } catch (err) {
        // console.log(err);
        setError(true);
      }
    };

    handleMount();
  }, [id]);

  if (error) {
    return <NotFound />;
  }

  return (
    <Row className="h-100">
      <Col className="py-2 p-0 p-lg-2" lg={8}>
        <PopularProfiles mobile />
        <Post {...post.results[0]} setPosts={setPost} postPage />
        <Container className={appStyles.Content}>
          {currentUser ? (
            <CommentCreateForm
              profile_id={currentUser.profile_id}
              profileImage={profile_image}
              post={id}
              setPost={setPost}
              setComments={setComments}
            />
          ) : comments.results.length ? (
            "Comments"
          ) : null}
          {comments.results.length ? (
            <InfiniteScroll
              children={comments.results
                .filter((comment) => comment.is_main_comment)
                .map((comment) => (
                  <Comment
                    key={comment.id}
                    {...comment}
                    setPost={setPost}
                    setComments={setComments}
                    is_main_comment={comment.is_main_comment}
                  />
                ))}
              dataLength={comments.results.length}
              loader={<Asset spinner />}
              hasMore={!!comments.next}
              next={() => fetchMoreData(comments, setComments)}
            />
          ) : currentUser ? (
            <span>No comments yet, be the first to comment!</span>
          ) : (
            <div>
              <span>No comments... yet!</span>
              <br />
              <span>
                Please{" "}
                <a href="/signup" style={{ textDecoration: "underline" }}>
                  Sign up
                </a>{" "}
                or
                <a href="/signin" style={{ textDecoration: "underline" }}>
                  {" "}
                  Sign In
                </a>{" "}
                to be the first to comment!
              </span>
            </div>
          )}
        </Container>
      </Col>
      <Col lg={4} className="d-none d-lg-block p-0 p-lg-2">
        <PopularProfiles />
      </Col>
    </Row>
  );
}

export default PostPage;
