import React, { useState, useEffect } from 'react';
import Container from 'react-bootstrap/Container';
import appStyles from '../../App.module.css';
import Asset from '../../components/Asset';
import { axiosReq } from '../../api/axiosDefaults';

const UserTopCategories = ({ mobile }) => {
    const [topCategories, setTopCategories] = useState([]);

    useEffect(() => {
        const fetchTopCategories = async () => {
            try {
                const { data } = await axiosReq.get("/user-top-categories/");
                const filteredCategories = data.filter(category => category.category__name !== null && category.category__id !== null);
                setTopCategories(filteredCategories);
            } catch (err) {
                console.log(err);
            }
        };

        fetchTopCategories();
    }, []);

    return (
        <Container className={`${appStyles.Content} ${mobile ? "d-lg-none text-center mb-3" : ""}`}>
            {topCategories.length ? (
                <>
                    <p>Top 5 User Categories</p>
                    {mobile ? (
                        // Für Mobile Ansicht
                        <div className="d-flex flex-wrap justify-content-around">
                            {topCategories.map((category) => (
                                <div key={category.category__id} className="mb-2">
                                    {category.category__name}
                                </div>
                            ))}
                        </div>
                    ) : (
                        // Für normale Ansicht
                        topCategories.map((category) => (
                            <div key={category.category__id} className="mb-2">
                                {category.category__name}
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

export default UserTopCategories;
