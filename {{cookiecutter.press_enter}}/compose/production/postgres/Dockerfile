{% if cookiecutter.use_postgis == "y" %}
FROM postgis/postgis
{% else %}
FROM postgres:13.2
{% endif %}


COPY ./compose/production/postgres/maintenance /usr/local/bin/maintenance
RUN chmod +x /usr/local/bin/maintenance/*
RUN mv /usr/local/bin/maintenance/* /usr/local/bin \
    && rmdir /usr/local/bin/maintenance
