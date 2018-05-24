from compas.datastructures.mesh import Mesh

from compas_pattern.datastructures.mesh import face_point
from compas_pattern.datastructures.mesh import insert_vertex_in_face
from compas_pattern.datastructures.mesh import add_vertex_from_vertices
from compas_pattern.datastructures.mesh import insert_vertices_in_halfedge

__author__     = ['Robin Oval']
__copyright__  = 'Copyright 2018, Block Research Group - ETH Zurich'
__license__    = 'MIT License'
__email__      = 'oval@arch.ethz.ch'

__all__ = [
    'vertex_pole',
    'face_pole',
    'edge_pole',
    'face_opening',
    'flat_corner_2',
    'flat_corner_3',
    'flat_corner_33',
    'split_35',
    'split_35_diag',
    'split_26',
    'simple_split',
    'double_split',
    'insert_pole',
    'insert_partial_pole',
    'pseudo_quad_split',
    'singular_boundary_1',
    'remove_tri',
    'rotate_vertex',
]

def vertex_pole(mesh, fkey, pole):

    if len(mesh.face_vertices(fkey)) != 4:
        return None
    if pole not in mesh.face_vertices(fkey):
        return None

    a = pole
    b = mesh.face_vertex_descendant(fkey, a)
    c = mesh.face_vertex_descendant(fkey, b)
    d = mesh.face_vertex_descendant(fkey, c)

    e = add_vertex_from_vertices(mesh, [a, b], [1, 2])
    f = add_vertex_from_vertices(mesh, [b, c], [1, 2])
    g = add_vertex_from_vertices(mesh, [c, d], [2, 1])
    h = add_vertex_from_vertices(mesh, [d, a], [2, 1])

    i = add_vertex_from_vertices(mesh, [a, b, c, d], [1, 1, 2, 1])
    
    mesh.delete_face(fkey)

    fkey_1 = mesh.add_face([a, a, i, h])
    fkey_2 = mesh.add_face([a, a, e, i])
    fkey_3 = mesh.add_face([e, b, f, i])
    fkey_4 = mesh.add_face([h, i, g, d])
    fkey_5 = mesh.add_face([i, f, c, g])

    insert_vertices_in_halfedge(mesh, b, a, [e])
    insert_vertices_in_halfedge(mesh, c, b, [f])
    insert_vertices_in_halfedge(mesh, d, c, [g])
    insert_vertices_in_halfedge(mesh, a, d, [h])

    return fkey_1, fkey_2, fkey_3, fkey_4, fkey_5

def face_pole(mesh, fkey):

    if len(mesh.face_vertices(fkey)) != 4:
        return None

    a, b, c, d = mesh.face_vertices(fkey)


    e = add_vertex_from_vertices(mesh, [a, b], [2, 1])
    f = add_vertex_from_vertices(mesh, [a, b], [1, 2])
    g = add_vertex_from_vertices(mesh, [b, c], [2, 1])
    h = add_vertex_from_vertices(mesh, [b, c], [1, 2])
    i = add_vertex_from_vertices(mesh, [c, d], [2, 1])
    j = add_vertex_from_vertices(mesh, [c, d], [1, 2])
    k = add_vertex_from_vertices(mesh, [d, a], [2, 1])
    l = add_vertex_from_vertices(mesh, [d, a], [1, 2])

    m = add_vertex_from_vertices(mesh, [a, b, c, d], [2, 1, 1, 1])
    n = add_vertex_from_vertices(mesh, [a, b, c, d], [1, 2, 1, 1])
    o = add_vertex_from_vertices(mesh, [a, b, c, d], [1, 1, 2, 1])
    p = add_vertex_from_vertices(mesh, [a, b, c, d], [1, 1, 1, 2])

    q = add_vertex_from_vertices(mesh, [a, b, c, d], [1, 1, 1, 1])

    mesh.delete_face(fkey)

    fkey_1 = mesh.add_face([a, e, m, l])
    fkey_2 = mesh.add_face([e, f, n, m])
    fkey_3 = mesh.add_face([f, b, g, n])
    fkey_4 = mesh.add_face([l, m, p, k])
    fkey_5 = mesh.add_face([m, q, q, p])
    fkey_6 = mesh.add_face([m, n, q, q])
    fkey_7 = mesh.add_face([q, q, n, o])
    fkey_8 = mesh.add_face([n, g, h, o])
    fkey_9 = mesh.add_face([p, q, q, o])
    fkey_10 = mesh.add_face([k, p, j, d])
    fkey_11 = mesh.add_face([p, o, i, j])
    fkey_12 = mesh.add_face([o, h, c, i])

    insert_vertices_in_halfedge(mesh, b, a, [f, e])
    insert_vertices_in_halfedge(mesh, c, b, [h, g])
    insert_vertices_in_halfedge(mesh, d, c, [j, i])
    insert_vertices_in_halfedge(mesh, a, d, [l, k])

    return fkey_1, fkey_2, fkey_3, fkey_4, fkey_5, fkey_6, fkey_7, fkey_8, fkey_9, fkey_10, fkey_11, fkey_12

def edge_pole(mesh, fkey, edge):

    u, v = edge

    if len(mesh.face_vertices(fkey)) != 4:
        return None
    if (u, v) not in mesh.face_halfedges(fkey) and (v, u) not in mesh.face_halfedges(fkey):
        return None

    if v in mesh.halfedge[u] and mesh.halfedge[u][v] == fkey:
        a = u
    else:
        a = v

    b = mesh.face_vertex_descendant(fkey, a)
    c = mesh.face_vertex_descendant(fkey, b)
    d = mesh.face_vertex_descendant(fkey, c)


    e = add_vertex_from_vertices(mesh, [a, b], [2, 1])
    f = add_vertex_from_vertices(mesh, [a, b], [1, 1])
    g = add_vertex_from_vertices(mesh, [a, b], [1, 2])
    h = add_vertex_from_vertices(mesh, [b, c], [1, 2])
    i = add_vertex_from_vertices(mesh, [c, d], [2, 1])
    j = add_vertex_from_vertices(mesh, [c, d], [1, 2])
    k = add_vertex_from_vertices(mesh, [d, a], [2, 1])

    l = add_vertex_from_vertices(mesh, [a, b, c, d], [1, 1, 1, 2])
    m = add_vertex_from_vertices(mesh, [a, b, c, d], [1, 1, 2, 1])
    
    mesh.delete_face(fkey)

    fkey_1 = mesh.add_face([a, e, l, k])
    fkey_2 = mesh.add_face([e, f, f, l])
    fkey_3 = mesh.add_face([l, f, f, m])
    fkey_4 = mesh.add_face([f, f, g, m])
    fkey_5 = mesh.add_face([g, b, h, m])
    fkey_6 = mesh.add_face([k, l, j, d])
    fkey_7 = mesh.add_face([l, m, i, j])
    fkey_8 = mesh.add_face([m, h, c, i])

    insert_vertices_in_halfedge(mesh, b, a, [g, f, e])
    insert_vertices_in_halfedge(mesh, c, b, [h])
    insert_vertices_in_halfedge(mesh, d, c, [j, i])
    insert_vertices_in_halfedge(mesh, a, d, [k])

    return fkey_1, fkey_2, fkey_3, fkey_4, fkey_5, fkey_6, fkey_7, fkey_8

def face_opening(mesh, fkey):

    if len(mesh.face_vertices(fkey)) != 4:
        return None

    a, b, c, d = mesh.face_vertices(fkey)

    e = add_vertex_from_vertices(mesh, [a, b, c, d], [2, 1, 1, 1])
    f = add_vertex_from_vertices(mesh, [a, b, c, d], [1, 2, 1, 1])
    g = add_vertex_from_vertices(mesh, [a, b, c, d], [1, 1, 2, 1])    
    h = add_vertex_from_vertices(mesh, [a, b, c, d], [1, 1, 1, 2])

    mesh.delete_face(fkey)

    fkey_1 = mesh.add_face([a, b, f, e])
    fkey_2 = mesh.add_face([b, c, g, f])
    fkey_3 = mesh.add_face([c, d, h, g])
    fkey_4 = mesh.add_face([d, a, e, h])

    return fkey_1, fkey_2, fkey_3, fkey_4

def flat_corner_2(mesh, fkey, corner):

    if len(mesh.face_vertices(fkey)) != 4:
        return None
    if corner not in mesh.face_vertices(fkey):
        return None

    a = corner
    b = mesh.face_vertex_descendant(fkey, a)
    c = mesh.face_vertex_descendant(fkey, b)
    d = mesh.face_vertex_descendant(fkey, c)

    e = add_vertex_from_vertices(mesh, [a, b, c, d], [1, 1, 1, 1])
    
    mesh.delete_face(fkey)

    fkey_1 = mesh.add_face([a, b, c, e])
    fkey_2 = mesh.add_face([a, e, c, d])

    return fkey_1, fkey_2

def flat_corner_3(mesh, fkey, corner):

    if len(mesh.face_vertices(fkey)) != 4:
        return None
    if corner not in mesh.face_vertices(fkey):
        return None

    a = corner
    b = mesh.face_vertex_descendant(fkey, a)
    c = mesh.face_vertex_descendant(fkey, b)
    d = mesh.face_vertex_descendant(fkey, c)

    e = add_vertex_from_vertices(mesh, [b, c], [1, 1])
    f = add_vertex_from_vertices(mesh, [c, d], [1, 1])
    g = add_vertex_from_vertices(mesh, [a, b, c, d], [1, 1, 1, 1])
    
    mesh.delete_face(fkey)

    fkey_1 = mesh.add_face([a, b, e, g])
    fkey_2 = mesh.add_face([e, c, f, g])
    fkey_3 = mesh.add_face([d, a, g, f])

    insert_vertices_in_halfedge(mesh, c, b, [e])
    insert_vertices_in_halfedge(mesh, d, c, [f])

    return fkey_1, fkey_2, fkey_3

def flat_corner_33(mesh, fkey, corner):

    if len(mesh.face_vertices(fkey)) != 4:
        return None
    if corner not in mesh.face_vertices(fkey):
        return None

    a = corner
    b = mesh.face_vertex_descendant(fkey, a)
    c = mesh.face_vertex_descendant(fkey, b)
    d = mesh.face_vertex_descendant(fkey, c)

    e = add_vertex_from_vertices(mesh, [d, a], [1, 1])
    f = add_vertex_from_vertices(mesh, [a, b], [1, 1])
    g = add_vertex_from_vertices(mesh, [b, c], [1, 1])
    h = add_vertex_from_vertices(mesh, [c, d], [1, 1])

    i = add_vertex_from_vertices(mesh, [a, b, c, d], [1, 1, 1, 2])
    j = add_vertex_from_vertices(mesh, [a, b, c, d], [1, 2, 1, 1])
    k = add_vertex_from_vertices(mesh, [a, b, c, d], [1, 1, 1, 1])

    mesh.delete_face(fkey)

    fkey_1 = mesh.add_face([a, f, j, k])
    fkey_2 = mesh.add_face([f, b, g, j])
    fkey_3 = mesh.add_face([j, g, c , k])
    fkey_4 = mesh.add_face([a, k, i, e])
    fkey_5 = mesh.add_face([k, c, h, i])
    fkey_6 = mesh.add_face([e, i, h, d])

    insert_vertices_in_halfedge(mesh, b, a, [f])
    insert_vertices_in_halfedge(mesh, c, b, [g])
    insert_vertices_in_halfedge(mesh, d, c, [h])
    insert_vertices_in_halfedge(mesh, a, d, [e])

    return fkey_1, fkey_2, fkey_3, fkey_4, fkey_5, fkey_6

def split_35(mesh, fkey, edge):

    u, v = edge

    if len(mesh.face_vertices(fkey)) != 4:
        return None
    if (u, v) not in mesh.face_halfedges(fkey) and (v, u) not in mesh.face_halfedges(fkey):
        return None

    if v in mesh.halfedge[u] and mesh.halfedge[u][v] == fkey:
        a = u
    else:
        a = v

    b = mesh.face_vertex_descendant(fkey, a)
    c = mesh.face_vertex_descendant(fkey, b)
    d = mesh.face_vertex_descendant(fkey, c)

    e = add_vertex_from_vertices(mesh, [a, b], [2, 1])
    f = add_vertex_from_vertices(mesh, [a, b], [1, 1])
    g = add_vertex_from_vertices(mesh, [a, b], [1, 2])
    h = add_vertex_from_vertices(mesh, [b, c], [1, 1])
    i = add_vertex_from_vertices(mesh, [b, c], [1, 2])
    j = add_vertex_from_vertices(mesh, [c, d], [1, 1])
    k = add_vertex_from_vertices(mesh, [d, a], [2, 1])
    l = add_vertex_from_vertices(mesh, [d, a], [1, 1])
    m = add_vertex_from_vertices(mesh, [a, b, c, d], [3, 2, 1, 2])
    n = add_vertex_from_vertices(mesh, [a, b, c, d], [2, 2, 1, 1])
    o = add_vertex_from_vertices(mesh, [a, b, c, d], [2, 3, 2, 1])
    p = add_vertex_from_vertices(mesh, [a, b, c, d], [1, 1, 2, 2])

    mesh.delete_face(fkey)

    fkey_1 = mesh.add_face([a, e, m, l])
    fkey_2 = mesh.add_face([e, f, n, m])
    fkey_3 = mesh.add_face([f, g, o, n])
    fkey_4 = mesh.add_face([g, b, h, o])
    fkey_5 = mesh.add_face([l, m, p, k])
    fkey_6 = mesh.add_face([m, n, o, p])
    fkey_7 = mesh.add_face([o, h, i, p])
    fkey_8 = mesh.add_face([k, p, j, d])
    fkey_9 = mesh.add_face([p, i, c, j])

    insert_vertices_in_halfedge(mesh, b, a, [g, f, e])
    insert_vertices_in_halfedge(mesh, c, b, [i, h])
    insert_vertices_in_halfedge(mesh, d, c, [j])
    insert_vertices_in_halfedge(mesh, a, d, [l, k])

    return fkey_1, fkey_2, fkey_3, fkey_4, fkey_5, fkey_6, fkey_7, fkey_8, fkey_9

def split_35_diag(mesh, fkey, corner):

    if len(mesh.face_vertices(fkey)) != 4:
        return None
    if corner not in mesh.face_vertices(fkey):
        return None

    a = corner
    b = mesh.face_vertex_descendant(fkey, a)
    c = mesh.face_vertex_descendant(fkey, b)
    d = mesh.face_vertex_descendant(fkey, c)

    e = add_vertex_from_vertices(mesh, [a, b], [2, 1])
    f = add_vertex_from_vertices(mesh, [a, b], [1, 2])
    g = add_vertex_from_vertices(mesh, [b, c], [1, 2])
    h = add_vertex_from_vertices(mesh, [c, d], [2, 1])
    i = add_vertex_from_vertices(mesh, [d, a], [2, 1])
    j = add_vertex_from_vertices(mesh, [d, a], [1, 2])
    k = add_vertex_from_vertices(mesh, [a, c], [2, 1])
    l = add_vertex_from_vertices(mesh, [a, c], [1, 2])

    mesh.delete_face(fkey)

    fkey_1 = mesh.add_face([a, e, k, j])
    fkey_2 = mesh.add_face([e, f, l, k])
    fkey_3 = mesh.add_face([f, b, g, l])
    fkey_4 = mesh.add_face([j, k, l, i])
    fkey_5 = mesh.add_face([i, l, h, d])
    fkey_6 = mesh.add_face([l, g, c, h])

    insert_vertices_in_halfedge(mesh, b, a, [f, e])
    insert_vertices_in_halfedge(mesh, c, b, [g])
    insert_vertices_in_halfedge(mesh, d, c, [h])
    insert_vertices_in_halfedge(mesh, a, d, [j, i])

    return fkey_1, fkey_2, fkey_3, fkey_4, fkey_5, fkey_6

def split_26(mesh, fkey, edge):

    u, v = edge

    if len(mesh.face_vertices(fkey)) != 4:
        return None
    if (u, v) not in mesh.face_halfedges(fkey) and (v, u) not in mesh.face_halfedges(fkey):
        return None

    if v in mesh.halfedge[u] and mesh.halfedge[u][v] == fkey:
        a = u
    else:
        a = v

    b = mesh.face_vertex_descendant(fkey, a)
    c = mesh.face_vertex_descendant(fkey, b)
    d = mesh.face_vertex_descendant(fkey, c)

    e = add_vertex_from_vertices(mesh, [a, b], [2, 1])
    f = add_vertex_from_vertices(mesh, [a, b], [1, 1])
    g = add_vertex_from_vertices(mesh, [a, b], [1, 2])
    h = add_vertex_from_vertices(mesh, [b, c], [1, 2])
    i = add_vertex_from_vertices(mesh, [c, d], [1, 1])
    j = add_vertex_from_vertices(mesh, [d, a], [2, 1])
    k = add_vertex_from_vertices(mesh, [a, b, c, d], [2, 2, 1, 1])
    l = add_vertex_from_vertices(mesh, [a, b, c, d], [1, 1, 1, 1])

    mesh.delete_face(fkey)

    fkey_1 = mesh.add_face([a, e, l, j])
    fkey_2 = mesh.add_face([e, f, k, l])
    fkey_3 = mesh.add_face([f, g, l, k])
    fkey_4 = mesh.add_face([g, b, h, l])
    fkey_5 = mesh.add_face([j, l, i, d])
    fkey_6 = mesh.add_face([l, h, c, i])

    insert_vertices_in_halfedge(mesh, b, a, [g, f, e])
    insert_vertices_in_halfedge(mesh, c, b, [h])
    insert_vertices_in_halfedge(mesh, d, c, [i])
    insert_vertices_in_halfedge(mesh, a, d, [j])

    return fkey_1, fkey_2, fkey_3, fkey_4, fkey_5, fkey_6

def simple_split(mesh, fkey, edge):

    u, v = edge

    if len(mesh.face_vertices(fkey)) != 4:
        return None
    if (u, v) not in mesh.face_halfedges(fkey) and (v, u) not in mesh.face_halfedges(fkey):
        return None

    if v in mesh.halfedge[u] and mesh.halfedge[u][v] == fkey:
        a = u
    else:
        a = v

    b = mesh.face_vertex_descendant(fkey, a)
    c = mesh.face_vertex_descendant(fkey, b)
    d = mesh.face_vertex_descendant(fkey, c)

    e = add_vertex_from_vertices(mesh, [a, b], [1, 1])
    f = add_vertex_from_vertices(mesh, [c, d], [1, 1])

    mesh.delete_face(fkey)

    fkey_1 = mesh.add_face([a, e, f, d])
    fkey_2 = mesh.add_face([e, b, c, f])

    insert_vertices_in_halfedge(mesh, b, a, [e])
    insert_vertices_in_halfedge(mesh, d, c, [f])

    return fkey_1, fkey_2

def double_split(mesh, fkey):

    if len(mesh.face_vertices(fkey)) != 4:
        return None

    a, b, c, d = mesh.face_vertices(fkey)

    e = add_vertex_from_vertices(mesh, [a, b], [1, 1])
    f = add_vertex_from_vertices(mesh, [b, c], [1, 1])
    g = add_vertex_from_vertices(mesh, [c, d], [1, 1])
    h = add_vertex_from_vertices(mesh, [d, a], [1, 1])
    i = add_vertex_from_vertices(mesh, [a, b, c, d], [1, 1, 1, 1])

    mesh.delete_face(fkey)

    fkey_1 = mesh.add_face([a, e, i, h])
    fkey_2 = mesh.add_face([e, b, f, i])
    fkey_3 = mesh.add_face([h, i, g, d])
    fkey_4 = mesh.add_face([i, f, c, g])

    insert_vertices_in_halfedge(mesh, b, a, [e])
    insert_vertices_in_halfedge(mesh, c, b, [f])
    insert_vertices_in_halfedge(mesh, d, c, [g])
    insert_vertices_in_halfedge(mesh, a, d, [h])

    return fkey_1, fkey_2, fkey_3, fkey_4

def insert_pole(mesh, fkey, pole):

    if len(mesh.face_vertices(fkey)) != 4:
        return None
    if pole not in mesh.face_vertices(fkey):
        return None

    a = pole
    b = mesh.face_vertex_descendant(fkey, a)
    c = mesh.face_vertex_descendant(fkey, b)
    d = mesh.face_vertex_descendant(fkey, c)

    mesh.delete_face(fkey)

    fkey_1 = mesh.add_face([a, a, b, c])
    fkey_2 = mesh.add_face([a, a, c, d])

    return fkey_1, fkey_2

def insert_partial_pole(mesh, fkey, pole, edge):

    u, v = edge
    
    if len(mesh.face_vertices(fkey)) != 4:
        return None
    if pole not in mesh.face_vertices(fkey):
        return None
    if (u, v) not in mesh.face_halfedges(fkey) and (v, u) not in mesh.face_halfedges(fkey):
        return None

    if v not in mesh.halfedge[u] or mesh.halfedge[u][v] != fkey:
        u, v = v, u

    a = pole
    b = mesh.face_vertex_descendant(fkey, a)
    c = mesh.face_vertex_descendant(fkey, b)
    d = mesh.face_vertex_descendant(fkey, c)

    if u != b and u != c:
        return None

    mesh.delete_face(fkey)

    e = add_vertex_from_vertices(mesh, [u, v], [1, 1])

    if u == b:
        fkey_1 = mesh.add_face([a, a, b, e])
        fkey_2 = mesh.add_face([a, e, c, d])

    if u == c:
        fkey_1 = mesh.add_face([a, b, c, e])
        fkey_2 = mesh.add_face([a, a, e, d])

    insert_vertices_in_halfedge(mesh, v, u, [e])

    return fkey_1, fkey_2

def pseudo_quad_split(mesh, fkey):

    face_vertices = mesh.face_vertices(fkey)
    if len(face_vertices) != 4:
        return None

    pole = None
    for i in range(len(face_vertices) - 1):
        if face_vertices[i - 1] == face_vertices[i]:
            pole = face_vertices[i]
    if pole is None:
        return None

    face_vertices.remove(pole)
    idx = face_vertices.index(pole)
    a = pole
    b = mesh.face_vertex_descendant(fkey, a)
    c = mesh.face_vertex_descendant(fkey, b)

    mesh.delete_face(fkey)

    d = add_vertex_from_vertices(mesh, [a, b], [1, 1])
    e = add_vertex_from_vertices(mesh, [b, c], [1, 1])
    f = add_vertex_from_vertices(mesh, [c, a], [1, 1])
    g = add_vertex_from_vertices(mesh, [a, b, c], [1, 1, 1])

    fkey_1 = mesh.add_face([a, d, g, f])
    fkey_2 = mesh.add_face([b, e, g, d])
    fkey_3 = mesh.add_face([c, f, g, e])

    insert_vertices_in_halfedge(mesh, b, a, [d])
    insert_vertices_in_halfedge(mesh, c, b, [e])
    insert_vertices_in_halfedge(mesh, a, c, [f])

    return fkey_1, fkey_2, fkey_3
    
def singular_boundary_1(mesh, edge, vkey):

    u, v = edge
    if vkey != u and vkey != v:
        return None

    if mesh.is_edge_on_boundary(u, v):
        return None
    if len(mesh.face_vertices(mesh.halfedge[u][v])) != 4 or len(mesh.face_vertices(mesh.halfedge[v][u])) != 4:
        return None

    if vkey == u:
        b = u
        e = v
    else:
        b = v
        e = u

    fkey_1 = mesh.halfedge[b][e]
    fkey_2 = mesh.halfedge[e][b]

    f = mesh.face_vertex_descendant(fkey_1, e)
    a = mesh.face_vertex_descendant(fkey_1, f)
    c = mesh.face_vertex_descendant(fkey_2, b)
    d = mesh.face_vertex_descendant(fkey_2, c)

    mesh.delete_face(fkey_1)
    mesh.delete_face(fkey_2)

    g = add_vertex_from_vertices(mesh, [d, e], [1, 1])
    h = add_vertex_from_vertices(mesh, [e, f], [1, 1])

    fkey_1 = mesh.add_face([a, b, h, f])
    fkey_2 = mesh.add_face([b, g, e, h])
    fkey_3 = mesh.add_face([b, c, d, g])

    insert_vertices_in_halfedge(mesh, e, d, [g])
    insert_vertices_in_halfedge(mesh, f, e, [h])

    return fkey_1, fkey_2, fkey_3

def singular_boundary_2(mesh, edge, vkey):

    u, v = edge
    if vkey != u and vkey != v:
        return None

    if mesh.is_edge_on_boundary(u, v):
        return None
    if len(mesh.face_vertices(mesh.halfedge[u][v])) != 4 or len(mesh.face_vertices(mesh.halfedge[v][u])) != 4:
        return None

    if vkey == u:
        b = u
        e = v
    else:
        b = v
        e = u

    fkey_1 = mesh.halfedge[b][e]
    fkey_2 = mesh.halfedge[e][b]

    f = mesh.face_vertex_descendant(fkey_1, e)
    a = mesh.face_vertex_descendant(fkey_1, f)
    c = mesh.face_vertex_descendant(fkey_2, b)
    d = mesh.face_vertex_descendant(fkey_2, c)

    mesh.delete_face(fkey_1)
    mesh.delete_face(fkey_2)

    g = add_vertex_from_vertices(mesh, [d, e], [2, 1])
    h = add_vertex_from_vertices(mesh, [d, e], [1, 2])
    i = add_vertex_from_vertices(mesh, [e, f], [2, 1])
    j = add_vertex_from_vertices(mesh, [e, f], [1, 2])

    fkey_1 = mesh.add_face([a, b, j, f])
    fkey_2 = mesh.add_face([b, e, i, j])
    fkey_3 = mesh.add_face([b, g, h, e])
    fkey_4 = mesh.add_face([b, c, d, g])

    insert_vertices_in_halfedge(mesh, e, d, [h, g])
    insert_vertices_in_halfedge(mesh, f, e, [j, i])

    return fkey_1, fkey_2, fkey_3

def remove_tri(mesh, fkey_tri, fkey_quad, pole, t = .5):

    if len(mesh.face_vertices(fkey_tri)) != 3 or len(mesh.face_vertices(fkey_quad)) != 4:
        return None

    if fkey_tri not in mesh.face_neighbours(fkey_quad):
        return None

    if pole not in mesh.face_vertices(fkey_tri) or pole not in mesh.face_vertices(fkey_quad):
        return None

    nbr = mesh.face_vertex_descendant(fkey_quad, pole)

    if nbr not in mesh.face_vertices(fkey_tri):
        d = pole
        e = nbr
        a = mesh.face_vertex_descendant(fkey_quad, e)
        b = mesh.face_vertex_descendant(fkey_quad, a)
        c = mesh.face_vertex_descendant(fkey_tri, b)

        mesh.delete_face(fkey_tri)
        mesh.delete_face(fkey_quad)

        f = add_vertex_from_vertices(mesh, [d, e], [1 - t, t])

        fkey_tri = mesh.add_face([a, b, f, e])
        fkey_quad = mesh.add_face([b, c, d, f])

        insert_vertices_in_halfedge(mesh, e, d, [f])

    else:
        b = pole
        d = nbr
        e = mesh.face_vertex_descendant(fkey_quad, d)
        a = mesh.face_vertex_descendant(fkey_quad, e)
        c = mesh.face_vertex_descendant(fkey_tri, b)

        mesh.delete_face(fkey_tri)
        mesh.delete_face(fkey_quad)

        f = add_vertex_from_vertices(mesh, [b, a], [1 - t, t])

        fkey_tri = mesh.add_face([a, f, d, e])
        fkey_quad = mesh.add_face([b, c, d, f])

        insert_vertices_in_halfedge(mesh, b, a, [f])

    return fkey_tri, fkey_quad

def rotate_vertex(mesh, vkey):

    if vkey not in mesh.vertices():
        return None
    if vkey in mesh.vertices_on_boundary():
        return None

    face_vertices = {}
    for nbr in mesh.vertex_neighbours(vkey, True):
        fkey_0 = mesh.halfedge[vkey][nbr]
        fkey_1 = mesh.halfedge[nbr][vkey]
        ukey = mesh.face_vertex_descendant(fkey_0, nbr)
        wkey = mesh.face_vertex_ancestor(fkey_1, nbr)
        face_vertices[fkey_0] = [ukey, vkey, wkey, nbr]

    for fkey, vertices in face_vertices.items():
        mesh.delete_face(fkey)
        mesh.add_face(vertices, fkey = fkey)

    return 0

# ==============================================================================
# Main
# ==============================================================================

if __name__ == '__main__':

    import compas

    vertices = [[0,0,0],[1,0,0],[1,1,0],[0,1,0],[2,.5,0]]
    faces = [[0,1,2,3],[1,4,2]]

    mesh = Mesh.from_vertices_and_faces(vertices, faces)

    remove_tri(mesh, 1, 0, 2)

    for fkey in mesh.faces():
        print mesh.face_vertices(fkey)

    print mesh