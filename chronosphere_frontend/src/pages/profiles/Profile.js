import React from "react";
import styles from "../../styles/Profile.module.css";
import btnStyles from "../../styles/Button.module.css";
import { useCurrentUser } from "../../contexts/CurrentUserContext";
import { Link } from "react-router-dom";
import Avatar from "../../components/Avatar";
import Button from "react-bootstrap/Button";
import { useSetProfileData } from "../../contexts/ProfileDataContext";

const Profile = (props) => {
  const { profile, mobile, imageSize = 55 } = props;
  const { id, following_id, image, owner } = profile;
  const currentUser = useCurrentUser();
  const is_owner = currentUser?.username === owner;
  const { handleFollow, handleUnfollow } = useSetProfileData();

  return (
    <div className={`my-3 d-flex align-items-center ${mobile && "flex-column"}`}>
      <Link to={`/profiles/${id}`} className="align-self-center">
        <Avatar src={image} height={imageSize} />
      </Link>
      <div className={`mx-2 ${styles.WordBreak}`}>
      <Link to={`/profiles/${id}`} className={`${styles.WordBreak} ${styles.profileLink}`}>
        <strong>{owner}</strong>
      </Link>
      </div>
      {!mobile && currentUser && !is_owner && (
        <div className={`text-right ml-auto`}>
          {following_id ? (
            <Button
              className={`${btnStyles.Button} ${btnStyles.BlackOutline}`}
              onClick={() => handleUnfollow(profile)}
            >
              Unfollow
            </Button>
          ) : (
            <Button
              className={`${btnStyles.Button} ${btnStyles.Black}`}
              onClick={() => handleFollow(profile)}
            >
              Follow
            </Button>
          )}
        </div>
      )}
    </div>
  );
};

export default Profile;
