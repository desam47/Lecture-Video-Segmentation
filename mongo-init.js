db.createUser(
        {
            user: "root",
            pwd: "MongoDB2020!",
            roles: [
                {
                    role: "root",
                    db: "topic_segmentation"
                }
            ]
        }
);
