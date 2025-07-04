from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercise_shema import CreateExerciseRequestSchema, CreateExerciseResponseSchema, \
    GetExercisesResponseSchema, ExerciseSchema, UpdateExerciseRequestSchema, \
    UpdateExerciseResponseSchema
from tools.assertions.assert_equal import assert_equal
from tools.assertions.errors import assert_internal_error_response


def assert_create_exercise_response(
        request: CreateExerciseRequestSchema,
        response: CreateExerciseResponseSchema,
):
    """
    Проверяет, что параметры запроса соотвествуют параметрам ответа

    :param request: Исходный запрос на создание задания.
    :param response: Ответ API с данными созданного задания.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    # Базовые поля курса
    assert_equal(response.exercise.course_id, request.course_id, "title")
    assert_equal(response.exercise.title, request.title, "title")
    assert_equal(response.exercise.max_score, request.max_score, "max_score")
    assert_equal(response.exercise.min_score, request.min_score, "min_score")
    assert_equal(response.exercise.description, request.description, "orderIndex")
    assert_equal(response.exercise.description, request.description, "description")
    assert_equal(response.exercise.estimated_time, request.estimated_time, "estimated_time")


def assert_exercise(
        actual: ExerciseSchema,
        expected: ExerciseSchema
):
    """
    Проверяет, что фактические данные упражнения соответствуют ожидаемым.

    :param actual: Фактические данные упражнения.
    :param expected: Ожидаемые данные упражнения.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """

    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.course_id, expected.course_id, "courseId")
    assert_equal(actual.max_score, expected.max_score, "maxScore")
    assert_equal(actual.min_score, expected.min_score, "minScore")
    assert_equal(actual.order_index, expected.order_index, "orderIndex")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimatedTime")


def assert_get_exercise_response(
        get_exercise_response: CreateExerciseResponseSchema,
        create_exercise_response: CreateExerciseResponseSchema
):
    """
    Проверяет, что ответ на получение упражнения соответствует ответу на его создание.

    :param get_exercise_response: Ответ API при запросе данных упражнения.
    :param create_exercise_response: Ответ API при создании упражнения.
    :raises AssertionError: Если данные упражнения не совпадают.
    """

    assert_exercise(get_exercise_response.exercise, create_exercise_response.exercise)


def assert_update_exercise_response(
            request: UpdateExerciseRequestSchema,
            response: UpdateExerciseResponseSchema
    ):
        """
        Проверяет, что ответ на обновление pf соответствует данным из запроса.

        :param request: Исходный запрос на обновление курса.
        :param response: Ответ API с обновленными данными курса.
        :raises AssertionError: Если хотя бы одно поле не совпадает.
        """
        if request.title is not None:
            assert_equal(response.exercise.title, request.title, "title")

        if request.max_score is not None:
            assert_equal(response.exercise.max_score, request.max_score, "max_score")

        if request.min_score is not None:
            assert_equal(response.exercise.min_score, request.min_score, "min_score")

        if request.order_index is not None:
            assert_equal(response.exercise.order_index, request.order_index, "order_index")

        if request.description is not None:
            assert_equal(response.exercise.description, request.description, "description")

        if request.estimated_time is not None:
            assert_equal(response.exercise.estimated_time, request.estimated_time, "estimated_time")


def assert_exercise_not_found_response(actual: InternalErrorResponseSchema):
    """
    Функция для проверки ошибки, если не нашли задание.

    :param actual: Фактический ответ.
    :raises AssertionError: Если фактический ответ не соответствует ошибке "Exercise not found"
    """
    # Ожидаемое сообщение об ошибке, если файл не найден
    expected = InternalErrorResponseSchema(details="Exercise not found")
    # Используем ранее созданную функцию для проверки внутренней ошибки
    assert_internal_error_response(actual, expected)


def assert_get_exercises_response(
        get_exercise_response: GetExercisesResponseSchema,
        create_exercise_response: CreateExerciseResponseSchema
):
    """
    Проверяет, что ответ на получение упражнения соответствует ответу на его создание.
    """
    actual_exercise = next(
        (exercise for exercise in get_exercise_response.exercises
         if exercise.id == create_exercise_response.exercise.id),
        None
    )
    assert_exercise(actual_exercise, create_exercise_response.exercise)