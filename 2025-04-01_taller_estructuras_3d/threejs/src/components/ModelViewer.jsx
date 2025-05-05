import React, { useEffect } from "react";
import { useGLTF, OrbitControls, Edges, Points } from "@react-three/drei";
import { Canvas } from "@react-three/fiber";
import * as THREE from "three";

export default function ModelViewer() {
  const { scene, nodes } = useGLTF("/modelos/kawashaki_ninja_h2.glb");

  // Reemplaza materiales oscuros por uno visible (gris claro)
  useEffect(() => {
    scene.traverse((child) => {
      if (child.isMesh) {
        child.material = new THREE.MeshStandardMaterial({
          color: "gray",
          metalness: 0.2,
          roughness: 0.7
        });
      }
    });
  }, [scene]);

  return (
    <Canvas camera={{ position: [3, 3, 3], fov: 45 }}>
      {/* Fondo blanco */}
      <color attach="background" args={["white"]} />

      {/* Iluminación fuerte */}
      <ambientLight intensity={1.5} />
      <directionalLight position={[5, 5, 5]} intensity={2} castShadow />
      <pointLight position={[0, 2, 2]} intensity={1.2} />

      {/* Modelo 3D */}
      <primitive object={scene} />

      {/* Aristas en negro */}
      <Edges
        geometry={nodes?.Mesh_0?.geometry || scene.children[0].geometry}
        scale={1.01}
        color="black"
        threshold={15}
      />

      {/* Vértices en rojo */}
      <Points
        geometry={nodes?.Mesh_0?.geometry || scene.children[0].geometry}
        scale={1}
      >
        <pointsMaterial
          color="red"
          size={5}
          sizeAttenuation={false}
        />
      </Points>


      {/* Control de cámara */}
      <OrbitControls />
    </Canvas>
  );
}
