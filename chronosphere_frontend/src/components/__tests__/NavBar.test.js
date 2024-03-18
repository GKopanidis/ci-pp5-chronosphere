import { render, screen, fireEvent } from "@testing-library/react";
import { BrowserRouter as Router } from "react-router-dom";
import NavBar from "../NavBar";
import { CurrentUserProvider } from "../../contexts/CurrentUserContext";

test("renders NavBar", () => {
  render(
    <Router>
      <NavBar />
    </Router>
  );

  //   screen.debug();
  const signInLink = screen.getByRole("link", { name: "Sign in" });
  expect(signInLink).toBeInTheDocument();
});

test("renders link to the user profile for a logged in user", async () => {
  render(
    <Router>
      <CurrentUserProvider>
        <NavBar />
      </CurrentUserProvider>
    </Router>
  );

  const profileAvatar = await screen.findByText('Profile');
  expect(profileAvatar).toBeInTheDocument();
});

test("renders sign in and sign up buttons again on log out", async () => {
    render(
      <Router>
        <CurrentUserProvider>
          <NavBar />
        </CurrentUserProvider>
      </Router>
    );
  
    const signOutLink = await screen.findByRole("link", { name: "Sign out" });
    fireEvent.click(signOutLink);
  
    const signInLink = await screen.findByRole("link", { name: "Sign in" });
    const signUpLink = await screen.findByRole("link", { name: "Sign up" });
  
    expect(signInLink).toBeInTheDocument();
    expect(signUpLink).toBeInTheDocument();
  });

test("renders navigation links for authenticated user", async () => {
    render(
        <Router>
            <CurrentUserProvider>
                <NavBar />
            </CurrentUserProvider>
        </Router>
    );

    const homeLink = await screen.findByRole("link", { name: "Home" });
    const feedLink = await screen.findByRole("link", { name: "Feed" });
    const likedLink = await screen.findByRole("link", { name: "Liked" });
    const addPostIcon = await screen.findByRole("link", { name: "Add post" });

    expect(homeLink).toBeInTheDocument();
    expect(feedLink).toBeInTheDocument();
    expect(likedLink).toBeInTheDocument();
    expect(addPostIcon).toBeInTheDocument();
});