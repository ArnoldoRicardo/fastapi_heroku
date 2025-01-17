import "bootstrap/dist/css/bootstrap.min.css";
import { Container, Row, Col, Modal } from "react-bootstrap";
import { SearchClient } from "./SearchClient";
import { SearchProduct } from "./SearchProduct";
import { TableProducts } from "./TableProducts";
import { Spinner } from "./General/Spinner";
import { FormPay } from "./FormPay";
import { useState, useEffect } from "react";
import axios from "axios";

const CreateNote = () => {
  const [nombre, setNombre] = useState("");
  const [ventas, setVentas] = useState([]);
  const [total, setTotal] = useState(0);
  const [anticipo, setAnticipo] = useState(0);
  const [fecha, setFecha] = useState(new Date());

  const handleAddVenta = (nombre, cantidad, total) => {
    setVentas([...ventas, { nombre, cantidad, total }]);
  };

  useEffect(() => {
    if (ventas) {
      const newTotal = ventas.reduce(
        (acc, curr) => acc + parseFloat(curr.total) * parseFloat(curr.cantidad),
        0
      );
      setTotal(newTotal);
    }
  }, [ventas]);

  const handleSave = () => {
    handleShow();
    const addNota = async () => {
      try {
        const response = await axios.post(
          "https://fathomless-atoll-57807.herokuapp.com/note",
          {
            cliente: nombre,
            ventas,
            total,
            anticipo,
            date: fecha,
          }
        );
        handleClose();
        handleCancel();
      } catch (e) {
        console.log(e);
      }
    };
    addNota();
  };

  const handleCancel = () => {
    setVentas([]);
    setAnticipo(0);
    setTotal(0);
    setNombre("");
    setFecha(0);
  };

  const [show, setShow] = useState(false);

  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);

  return (
    <Container>
      <h3>Crear nueva nota</h3>
      <Row>
        <Col>
          <SearchClient
            nombre={nombre}
            setNombre={setNombre}
            setFecha={setFecha}
            fecha={fecha}
          />
        </Col>
      </Row>
      <Row>
        <Col>
          <hr />
          <SearchProduct handleAddVenta={handleAddVenta} />
        </Col>
      </Row>
      <Row>
        <Col>
          <hr />
          <TableProducts ventas={ventas} />
        </Col>
      </Row>
      <Row>
        <Col>
          <FormPay
            total={total}
            anticipo={anticipo}
            setAnticipo={setAnticipo}
            handleSave={handleSave}
            handleCancel={handleCancel}
          />
        </Col>
      </Row>

      <Modal show={show} onHide={handleClose}>
        <Modal.Header>
          <Modal.Title>Cargando nota</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <Spinner />
        </Modal.Body>
      </Modal>
    </Container>
  );
};

export default CreateNote;
