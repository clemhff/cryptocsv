def numberRows(table):
    return """
             SELECT max(id) FROM {0};
           """.format(table)

def selectNLines(table, min, max):
    return """
             SELECT *
             FROM {0}
             WHERE id >= {1}
                AND id < {2}
             ;
           """.format(table, min, max)
